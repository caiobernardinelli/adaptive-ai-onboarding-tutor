import re

ID_PATTERN = re.compile(r"[a-z0-9][a-z0-9_]*")
VERSION_PATTERN = re.compile(r"\d+\.\d+")

ROOT_FIELDS = {
    "schema_version",
    "graph_id",
    "graph_version",
    "primary_entry_domain",
    "domains",
    "concepts",
    "relationships",
}

NODE_FIELDS = {
    "id",
    "name",
    "description",
    "learning_objective",
}

RELATIONSHIP_FIELDS = {
    "from",
    "to",
    "type",
}

ALLOWED_RELATIONSHIP_TYPES = {
    "contains",
    "prerequisite_for",
}


def _is_valid_id(value):
    return isinstance(value, str) and ID_PATTERN.fullmatch(value) is not None


def _is_non_empty_string(value):
    return isinstance(value, str) and bool(value.strip())


def _is_valid_version(value):
    return isinstance(value, str) and VERSION_PATTERN.fullmatch(value) is not None


def validate_learning_graph(graph):
    errors = []

    # ---------------------------------------------------------
    # 1. ROOT
    # ---------------------------------------------------------

    if not isinstance(graph, dict):
        errors.append(
            {
                "code": "invalid_root_type",
                "path": "$",
                "message": "The Learning Graph must be a YAML object/dictionary.",
            }
        )
        return errors

    required_fields = [
        "schema_version",
        "graph_id",
        "graph_version",
        "primary_entry_domain",
        "domains",
        "concepts",
        "relationships",
    ]

    for field in required_fields:
        if field not in graph:
            errors.append(
                {
                    "code": f"missing_{field}",
                    "path": field,
                    "message": f"The {field} field is required.",
                }
            )

    # 1. schema_version
    if "schema_version" in graph:
        if not _is_valid_version(graph["schema_version"]):
            errors.append(
                {
                    "code": "invalid_schema_version",
                    "path": "schema_version",
                    "message": (
                        "The schema_version field must be a valid version string."
                    ),
                }
            )

    # 2. graph_id
    if "graph_id" in graph:
        if not _is_valid_id(graph["graph_id"]):
            errors.append(
                {
                    "code": "invalid_graph_id",
                    "path": "graph_id",
                    "message": (
                        "The graph_id field must be a valid snake_case ID."
                    ),
                }
            )

    # 3. graph_version
    if "graph_version" in graph:
        if not _is_valid_version(graph["graph_version"]):
            errors.append(
                {
                    "code": "invalid_graph_version",
                    "path": "graph_version",
                    "message": (
                        "The graph_version field must be a valid version string."
                    ),
                }
            )

    # 4. primary_entry_domain
    if "primary_entry_domain" in graph:
        if not _is_valid_id(graph["primary_entry_domain"]):
            errors.append(
                {
                    "code": "invalid_primary_entry_domain",
                    "path": "primary_entry_domain",
                    "message": (
                        "The primary_entry_domain field must contain a valid ID."
                    ),
                }
            )

    # 5, 6 and 7. fields that must be lists
    list_fields = [
        "domains",
        "concepts",
        "relationships",
    ]

    for field in list_fields:
        if field in graph and not isinstance(graph[field], list):
            errors.append(
                {
                    "code": f"invalid_{field}_type",
                    "path": field,
                    "message": f"The {field} field must be a list.",
                }
            )

    # 8. no unknown fields at the root
    for field in graph:
        if field not in ROOT_FIELDS:
            errors.append(
                {
                    "code": "unknown_root_field",
                    "path": field,
                    "message": (
                        f"The {field} field is not allowed at the Learning Graph root."
                    ),
                }
            )

    # Collections that are not lists cannot be validated internally.
    domains = graph.get("domains")
    concepts = graph.get("concepts")
    relationships = graph.get("relationships")

    valid_domains_list = isinstance(domains, list)
    valid_concepts_list = isinstance(concepts, list)
    valid_relationships_list = isinstance(relationships, list)

    # ---------------------------------------------------------
    # 2. DOMAINS AND CONCEPTS
    # ---------------------------------------------------------

    domain_ids = set()
    concept_ids = set()
    all_ids = set()

    valid_domains = []
    valid_concepts = []

    # 9. at least one Domain
    if valid_domains_list and len(domains) == 0:
        errors.append(
            {
                "code": "missing_domains",
                "path": "domains",
                "message": "The Learning Graph must contain at least one Domain.",
            }
        )

    if valid_domains_list:
        for index, domain in enumerate(domains):
            path = f"domains[{index}]"

            # Structural guard so validation can continue safely.
            if not isinstance(domain, dict):
                errors.append(
                    {
                        "code": "invalid_domain_type",
                        "path": path,
                        "message": "Each Domain must be an object/dictionary.",
                    }
                )
                continue

            valid_domains.append(domain)

            # The Domain schema is closed.
            for field in domain:
                if field not in NODE_FIELDS:
                    errors.append(
                        {
                            "code": "unknown_domain_field",
                            "path": f"{path}.{field}",
                            "message": (f"The {field} field is not allowed in a Domain."),
                        }
                    )

            # 10. valid ID
            domain_id = domain.get("id")

            if not _is_valid_id(domain_id):
                errors.append(
                    {
                        "code": "invalid_domain_id",
                        "path": f"{path}.id",
                        "message": "A Domain must have a valid ID.",
                    }
                )
            else:
                # 11. globally unique IDs
                if domain_id in all_ids:
                    errors.append(
                        {
                            "code": "duplicate_node_id",
                            "path": f"{path}.id",
                            "message": (
                                f"The ID {domain_id} is duplicated in the Learning Graph."
                            ),
                        }
                    )
                else:
                    all_ids.add(domain_id)
                    domain_ids.add(domain_id)

            # 12, 13, 14 e 15.
            required_text_fields = [
                "name",
                "description",
                "learning_objective",
            ]

            for field in required_text_fields:
                if field not in domain:
                    errors.append(
                        {
                            "code": f"missing_domain_{field}",
                            "path": f"{path}.{field}",
                            "message": (f"The {field} field is required in a Domain."),
                        }
                    )
                elif not _is_non_empty_string(domain[field]):
                    errors.append(
                        {
                            "code": f"invalid_domain_{field}",
                            "path": f"{path}.{field}",
                            "message": (
                                f"The Domain {field} field must be "
                                "a non-empty string."
                            ),
                        }
                    )

    if valid_concepts_list:
        for index, concept in enumerate(concepts):
            path = f"concepts[{index}]"

            if not isinstance(concept, dict):
                errors.append(
                    {
                        "code": "invalid_concept_type",
                        "path": path,
                        "message": "Each Concept must be an object/dictionary.",
                    }
                )
                continue

            valid_concepts.append(concept)

            for field in concept:
                if field not in NODE_FIELDS:
                    errors.append(
                        {
                            "code": "unknown_concept_field",
                            "path": f"{path}.{field}",
                            "message": (f"The {field} field is not allowed in a Concept."),
                        }
                    )

            concept_id = concept.get("id")

            # 10. valid ID
            if not _is_valid_id(concept_id):
                errors.append(
                    {
                        "code": "invalid_concept_id",
                        "path": f"{path}.id",
                        "message": "A Concept must have a valid ID.",
                    }
                )
            else:
                # 11. globally unique IDs
                if concept_id in all_ids:
                    errors.append(
                        {
                            "code": "duplicate_node_id",
                            "path": f"{path}.id",
                            "message": (
                                f"The ID {concept_id} is duplicated in the Learning Graph."
                            ),
                        }
                    )
                else:
                    all_ids.add(concept_id)
                    concept_ids.add(concept_id)

            # 12, 13, 14 e 15.
            required_text_fields = [
                "name",
                "description",
                "learning_objective",
            ]

            for field in required_text_fields:
                if field not in concept:
                    errors.append(
                        {
                            "code": f"missing_concept_{field}",
                            "path": f"{path}.{field}",
                            "message": (f"The {field} field is required in a Concept."),
                        }
                    )
                elif not _is_non_empty_string(concept[field]):
                    errors.append(
                        {
                            "code": f"invalid_concept_{field}",
                            "path": f"{path}.{field}",
                            "message": (
                                f"The Concept {field} field must be "
                                "a non-empty string."
                            ),
                        }
                    )

    # ---------------------------------------------------------
    # 3. RELATIONSHIPS
    # ---------------------------------------------------------

    valid_relationships = []

    if valid_relationships_list:
        relationship_keys = set()

        for index, relationship in enumerate(relationships):
            path = f"relationships[{index}]"

            if not isinstance(relationship, dict):
                errors.append(
                    {
                        "code": "invalid_relationship_type",
                        "path": path,
                        "message": ("Each relationship must be an object/dictionary."),
                    }
                )
                continue

            # Relationships contain exactly from, to, and type.
            for field in relationship:
                if field not in RELATIONSHIP_FIELDS:
                    errors.append(
                        {
                            "code": "unknown_relationship_field",
                            "path": f"{path}.{field}",
                            "message": (
                                f"The {field} field is not allowed in a relationship."
                            ),
                        }
                    )

            missing_relationship_field = False

            for field in RELATIONSHIP_FIELDS:
                if field not in relationship:
                    errors.append(
                        {
                            "code": f"missing_relationship_{field}",
                            "path": f"{path}.{field}",
                            "message": (
                                f"The {field} field is required in a relationship."
                            ),
                        }
                    )
                    missing_relationship_field = True

            if missing_relationship_field:
                continue

            from_id = relationship["from"]
            to_id = relationship["to"]
            relationship_type = relationship["type"]

            # 20. allowed type
            if relationship_type not in ALLOWED_RELATIONSHIP_TYPES:
                errors.append(
                    {
                        "code": "invalid_relationship_kind",
                        "path": f"{path}.type",
                        "message": (f"The relationship type {relationship_type} is not allowed."),
                    }
                )
                continue

            valid_relationships.append(relationship)

            # 19. referenced IDs must exist
            if from_id not in all_ids:
                errors.append(
                    {
                        "code": "unknown_relationship_from",
                        "path": f"{path}.from",
                        "message": (f"The source node {from_id} does not exist."),
                    }
                )

            if to_id not in all_ids:
                errors.append(
                    {
                        "code": "unknown_relationship_to",
                        "path": f"{path}.to",
                        "message": (f"The target node {to_id} does not exist."),
                    }
                )

            # 21. duplicate relationship
            relationship_key = (
                from_id,
                to_id,
                relationship_type,
            )

            if relationship_key in relationship_keys:
                errors.append(
                    {
                        "code": "duplicate_relationship",
                        "path": path,
                        "message": ("The from/to/type combination is duplicated."),
                    }
                )
            else:
                relationship_keys.add(relationship_key)

            if relationship_type == "contains":
                # 18. contains is always DOMAIN -> CONCEPT
                if from_id in all_ids and from_id not in domain_ids:
                    errors.append(
                        {
                            "code": "invalid_contains_source",
                            "path": f"{path}.from",
                            "message": ("The source of contains must be a Domain."),
                        }
                    )

                if to_id in all_ids and to_id not in concept_ids:
                    errors.append(
                        {
                            "code": "invalid_contains_target",
                            "path": f"{path}.to",
                            "message": ("The target of contains must be a Concept."),
                        }
                    )

            if relationship_type == "prerequisite_for":
                # 22. self-reference
                if from_id == to_id:
                    errors.append(
                        {
                            "code": "prerequisite_self_reference",
                            "path": path,
                            "message": (
                                "A prerequisite_for relationship "
                                "cannot point to itself."
                            ),
                        }
                    )

                # 23. DOMAIN -> CONCEPT not allowed
                if from_id in domain_ids and to_id in concept_ids:
                    errors.append(
                        {
                            "code": "invalid_domain_to_concept_prerequisite",
                            "path": path,
                            "message": (
                                "prerequisite_for cannot connect "
                                "a Domain directly to a Concept."
                            ),
                        }
                    )

                # 24. CONCEPT -> DOMAIN not allowed
                if from_id in concept_ids and to_id in domain_ids:
                    errors.append(
                        {
                            "code": "invalid_concept_to_domain_prerequisite",
                            "path": path,
                            "message": (
                                "prerequisite_for cannot connect "
                                "a Concept directly to a Domain."
                            ),
                        }
                    )

    # ---------------------------------------------------------
    # 4. MEMBERSHIP: DOMAIN --contains--> CONCEPT
    # ---------------------------------------------------------

    concept_domains = {}
    domain_concept_counts = {domain_id: 0 for domain_id in domain_ids}

    for relationship in valid_relationships:
        if relationship["type"] != "contains":
            continue

        from_id = relationship["from"]
        to_id = relationship["to"]

        if from_id not in domain_ids or to_id not in concept_ids:
            continue

        domain_concept_counts[from_id] += 1

        if to_id not in concept_domains:
            concept_domains[to_id] = []

        concept_domains[to_id].append(from_id)

    # 16. each Domain contains at least two Concepts
    for domain_id in domain_ids:
        if domain_concept_counts.get(domain_id, 0) < 2:
            errors.append(
                {
                    "code": "domain_has_too_few_concepts",
                    "path": f"domains.{domain_id}",
                    "message": (
                        f"The Domain {domain_id} must contain at least two Concepts."
                    ),
                }
            )

    # 17. each Concept has exactly one contains relationship
    for concept_id in concept_ids:
        memberships = concept_domains.get(concept_id, [])

        if len(memberships) != 1:
            errors.append(
                {
                    "code": "invalid_concept_membership_count",
                    "path": f"concepts.{concept_id}",
                    "message": (
                        f"The Concept {concept_id} must belong "
                        "to exactly one Domain through contains."
                    ),
                }
            )

    # ---------------------------------------------------------
    # 5. PREREQUISITES
    # ---------------------------------------------------------

    prerequisite_edges = []

    for relationship in valid_relationships:
        if relationship["type"] != "prerequisite_for":
            continue

        from_id = relationship["from"]
        to_id = relationship["to"]

        if from_id not in all_ids or to_id not in all_ids:
            continue

        prerequisite_edges.append((from_id, to_id))

        # 25. Concept prerequisites stay within the same Domain
        if from_id in concept_ids and to_id in concept_ids:
            from_domains = concept_domains.get(from_id, [])
            to_domains = concept_domains.get(to_id, [])

            if (
                len(from_domains) == 1
                and len(to_domains) == 1
                and from_domains[0] != to_domains[0]
            ):
                errors.append(
                    {
                        "code": "cross_domain_concept_prerequisite",
                        "path": (f"prerequisite_for.{from_id}->{to_id}"),
                        "message": (
                            "Concept prerequisites must remain "
                            "within the same Domain."
                        ),
                    }
                )

    # 26. prerequisite graph must be acyclic
    adjacency = {node_id: [] for node_id in all_ids}

    for from_id, to_id in prerequisite_edges:
        adjacency[from_id].append(to_id)

    visit_state = {node_id: 0 for node_id in all_ids}

    cycle_found = False

    def visit(node_id):
        nonlocal cycle_found

        if visit_state[node_id] == 1:
            cycle_found = True
            return

        if visit_state[node_id] == 2:
            return

        visit_state[node_id] = 1

        for neighbor in adjacency[node_id]:
            visit(neighbor)

        visit_state[node_id] = 2

    for node_id in all_ids:
        if visit_state[node_id] == 0:
            visit(node_id)

    if cycle_found:
        errors.append(
            {
                "code": "prerequisite_cycle",
                "path": "relationships",
                "message": ("The prerequisite_for graph must be acyclic."),
            }
        )

    # ---------------------------------------------------------
    # 6. PRIMARY ENTRY DOMAIN
    # ---------------------------------------------------------

    primary_entry_domain = graph.get("primary_entry_domain")

    if (
        _is_valid_id(primary_entry_domain)
        and valid_domains_list
        and valid_concepts_list
    ):
        # 27 and 28. must exist and be a Domain
        if primary_entry_domain not in all_ids:
            errors.append(
                {
                    "code": "primary_entry_domain_not_found",
                    "path": "primary_entry_domain",
                    "message": (
                        "The primary_entry_domain must reference an existing node."
                    ),
                }
            )

        elif primary_entry_domain not in domain_ids:
            errors.append(
                {
                    "code": "primary_entry_domain_not_domain",
                    "path": "primary_entry_domain",
                    "message": ("The primary_entry_domain must reference a Domain."),
                }
            )

        else:
            # 29. must be a Root Domain:
            # it cannot have another Domain as a prerequisite.
            has_domain_prerequisite = any(
                from_id in domain_ids and to_id == primary_entry_domain
                for from_id, to_id in prerequisite_edges
            )

            if has_domain_prerequisite:
                errors.append(
                    {
                        "code": "primary_entry_domain_not_root",
                        "path": "primary_entry_domain",
                        "message": ("The primary_entry_domain must be a Root Domain."),
                    }
                )

    return errors
