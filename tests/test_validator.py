from src.learning_graph.validator import validate_learning_graph


def make_valid_graph():
    return {
        "schema_version": "0.1",
        "graph_id": "test_graph",
        "graph_version": "0.2",
        "primary_entry_domain": "domain_a",
        "domains": [
            {
                "id": "domain_a",
                "name": "Domain A",
                "description": "Description of Domain A.",
                "learning_objective": "Learn Domain A.",
            }
        ],
        "concepts": [
            {
                "id": "concept_a",
                "name": "Concept A",
                "description": "Description of Concept A.",
                "learning_objective": "Learn Concept A.",
            },
            {
                "id": "concept_b",
                "name": "Concept B",
                "description": "Description of Concept B.",
                "learning_objective": "Learn Concept B.",
            },
        ],
        "relationships": [
            {
                "from": "domain_a",
                "to": "concept_a",
                "type": "contains",
            },
            {
                "from": "domain_a",
                "to": "concept_b",
                "type": "contains",
            },
        ],
    }


def test_invalid_domain_id_returns_error():
    graph = make_valid_graph()
    graph["domains"][0]["id"] = "Domain A"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_domain_id" for error in errors)


def test_missing_domain_name_returns_error():
    graph = make_valid_graph()
    del graph["domains"][0]["name"]

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "missing_domain_name" for error in errors)


def test_empty_domain_description_returns_error():
    graph = make_valid_graph()
    graph["domains"][0]["description"] = "   "

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_domain_description" for error in errors)


def test_unknown_domain_field_returns_error():
    graph = make_valid_graph()
    graph["domains"][0]["priority"] = 1

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "unknown_domain_field" for error in errors)


def test_invalid_concept_id_returns_error():
    graph = make_valid_graph()
    graph["concepts"][0]["id"] = "Concept A"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_concept_id" for error in errors)


def test_missing_concept_learning_objective_returns_error():
    graph = make_valid_graph()
    del graph["concepts"][0]["learning_objective"]

    errors = validate_learning_graph(graph)

    assert any(
        error["code"] == "missing_concept_learning_objective" for error in errors
    )


def test_duplicate_node_id_returns_error():
    graph = make_valid_graph()
    graph["concepts"][0]["id"] = "domain_a"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "duplicate_node_id" for error in errors)


def test_invalid_root_type_returns_error():
    errors = validate_learning_graph(None)

    assert errors == [
        {
            "code": "invalid_root_type",
            "path": "$",
            "message": "The Learning Graph must be a YAML object/dictionary.",
        }
    ]


def test_missing_required_root_fields_returns_errors():
    errors = validate_learning_graph({})

    assert errors == [
        {
            "code": "missing_schema_version",
            "path": "schema_version",
            "message": "The schema_version field is required.",
        },
        {
            "code": "missing_graph_id",
            "path": "graph_id",
            "message": "The graph_id field is required.",
        },
        {
            "code": "missing_graph_version",
            "path": "graph_version",
            "message": "The graph_version field is required.",
        },
        {
            "code": "missing_primary_entry_domain",
            "path": "primary_entry_domain",
            "message": "The primary_entry_domain field is required.",
        },
        {
            "code": "missing_domains",
            "path": "domains",
            "message": "The domains field is required.",
        },
        {
            "code": "missing_concepts",
            "path": "concepts",
            "message": "The concepts field is required.",
        },
        {
            "code": "missing_relationships",
            "path": "relationships",
            "message": "The relationships field is required.",
        },
    ]


def test_list_fields_with_invalid_types_return_errors():
    graph = {
        "schema_version": "0.1",
        "graph_id": "test_graph",
        "graph_version": "0.2",
        "primary_entry_domain": "contact_center_fundamentals",
        "domains": {},
        "concepts": "invalid",
        "relationships": None,
    }

    errors = validate_learning_graph(graph)

    assert errors == [
        {
            "code": "invalid_domains_type",
            "path": "domains",
            "message": "The domains field must be a list.",
        },
        {
            "code": "invalid_concepts_type",
            "path": "concepts",
            "message": "The concepts field must be a list.",
        },
        {
            "code": "invalid_relationships_type",
            "path": "relationships",
            "message": "The relationships field must be a list.",
        },
    ]


def test_unknown_root_field_returns_error():
    graph = make_valid_graph()
    graph["author"] = "Caio"

    errors = validate_learning_graph(graph)

    assert errors == [
        {
            "code": "unknown_root_field",
            "path": "author",
            "message": "The author field is not allowed at the Learning Graph root.",
        }
    ]


def test_invalid_schema_version_returns_error():
    graph = make_valid_graph()
    graph["schema_version"] = ""

    errors = validate_learning_graph(graph)

    assert errors == [
        {
            "code": "invalid_schema_version",
            "path": "schema_version",
            "message": "The schema_version field must be a valid version string.",
        }
    ]


def test_invalid_graph_id_returns_error():
    graph = make_valid_graph()
    graph["graph_id"] = "Test Graph"

    errors = validate_learning_graph(graph)

    assert errors == [
        {
            "code": "invalid_graph_id",
            "path": "graph_id",
            "message": "The graph_id field must be a valid snake_case ID.",
        }
    ]


def test_unknown_relationship_type_returns_error():
    graph = make_valid_graph()
    graph["relationships"][0]["type"] = "depends_on"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_relationship_kind" for error in errors)


def test_relationship_from_unknown_node_returns_error():
    graph = make_valid_graph()
    graph["relationships"][0]["from"] = "unknown_domain"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "unknown_relationship_from" for error in errors)


def test_relationship_to_unknown_node_returns_error():
    graph = make_valid_graph()
    graph["relationships"][0]["to"] = "unknown_concept"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "unknown_relationship_to" for error in errors)


def test_duplicate_relationship_returns_error():
    graph = make_valid_graph()
    graph["relationships"].append(
        {
            "from": "domain_a",
            "to": "concept_a",
            "type": "contains",
        }
    )

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "duplicate_relationship" for error in errors)


def test_contains_requires_domain_as_source():
    graph = make_valid_graph()
    graph["relationships"][0] = {
        "from": "concept_b",
        "to": "concept_a",
        "type": "contains",
    }

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_contains_source" for error in errors)


def test_contains_requires_concept_as_target():
    graph = make_valid_graph()
    graph["relationships"][0] = {
        "from": "domain_a",
        "to": "domain_a",
        "type": "contains",
    }

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_contains_target" for error in errors)


def test_prerequisite_self_reference_returns_error():
    graph = make_valid_graph()
    graph["relationships"].append(
        {
            "from": "concept_a",
            "to": "concept_a",
            "type": "prerequisite_for",
        }
    )

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "prerequisite_self_reference" for error in errors)


def test_domain_to_concept_prerequisite_returns_error():
    graph = make_valid_graph()
    graph["relationships"].append(
        {
            "from": "domain_a",
            "to": "concept_a",
            "type": "prerequisite_for",
        }
    )

    errors = validate_learning_graph(graph)

    assert any(
        error["code"] == "invalid_domain_to_concept_prerequisite" for error in errors
    )


def test_concept_to_domain_prerequisite_returns_error():
    graph = make_valid_graph()
    graph["relationships"].append(
        {
            "from": "concept_a",
            "to": "domain_a",
            "type": "prerequisite_for",
        }
    )

    errors = validate_learning_graph(graph)

    assert any(
        error["code"] == "invalid_concept_to_domain_prerequisite" for error in errors
    )


def test_cross_domain_concept_prerequisite_returns_error():
    graph = make_valid_graph()

    graph["domains"].append(
        {
            "id": "domain_b",
            "name": "Domain B",
            "description": "Description of Domain B.",
            "learning_objective": "Learn Domain B.",
        }
    )

    graph["concepts"].extend(
        [
            {
                "id": "concept_c",
                "name": "Concept C",
                "description": "Description of Concept C.",
                "learning_objective": "Learn Concept C.",
            },
            {
                "id": "concept_d",
                "name": "Concept D",
                "description": "Description of Concept D.",
                "learning_objective": "Learn Concept D.",
            },
        ]
    )

    graph["relationships"].extend(
        [
            {
                "from": "domain_b",
                "to": "concept_c",
                "type": "contains",
            },
            {
                "from": "domain_b",
                "to": "concept_d",
                "type": "contains",
            },
            {
                "from": "concept_a",
                "to": "concept_c",
                "type": "prerequisite_for",
            },
        ]
    )

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "cross_domain_concept_prerequisite" for error in errors)


def test_prerequisite_cycle_returns_error():
    graph = make_valid_graph()

    graph["relationships"].extend(
        [
            {
                "from": "concept_a",
                "to": "concept_b",
                "type": "prerequisite_for",
            },
            {
                "from": "concept_b",
                "to": "concept_a",
                "type": "prerequisite_for",
            },
        ]
    )

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "prerequisite_cycle" for error in errors)


def test_domain_with_fewer_than_two_concepts_returns_error():
    graph = make_valid_graph()

    graph["concepts"] = [
        {
            "id": "concept_a",
            "name": "Concept A",
            "description": "Description of Concept A.",
            "learning_objective": "Learn Concept A.",
        }
    ]

    graph["relationships"] = [
        {
            "from": "domain_a",
            "to": "concept_a",
            "type": "contains",
        }
    ]

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "domain_has_too_few_concepts" for error in errors)


def test_concept_without_contains_returns_error():
    graph = make_valid_graph()

    graph["relationships"] = [
        {
            "from": "domain_a",
            "to": "concept_b",
            "type": "contains",
        }
    ]

    errors = validate_learning_graph(graph)

    assert any(
        error["code"] == "invalid_concept_membership_count"
        and error["path"] == "concepts.concept_a"
        for error in errors
    )


def test_concept_with_multiple_contains_returns_error():
    graph = make_valid_graph()

    graph["domains"].append(
        {
            "id": "domain_b",
            "name": "Domain B",
            "description": "Description of Domain B.",
            "learning_objective": "Learn Domain B.",
        }
    )

    graph["concepts"].extend(
        [
            {
                "id": "concept_c",
                "name": "Concept C",
                "description": "Description of Concept C.",
                "learning_objective": "Learn Concept C.",
            },
            {
                "id": "concept_d",
                "name": "Concept D",
                "description": "Description of Concept D.",
                "learning_objective": "Learn Concept D.",
            },
        ]
    )

    graph["relationships"].extend(
        [
            {
                "from": "domain_b",
                "to": "concept_c",
                "type": "contains",
            },
            {
                "from": "domain_b",
                "to": "concept_d",
                "type": "contains",
            },
            {
                "from": "domain_b",
                "to": "concept_a",
                "type": "contains",
            },
        ]
    )

    errors = validate_learning_graph(graph)

    assert any(
        error["code"] == "invalid_concept_membership_count"
        and error["path"] == "concepts.concept_a"
        for error in errors
    )


def test_primary_entry_domain_must_exist():
    graph = make_valid_graph()
    graph["primary_entry_domain"] = "unknown_domain"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "primary_entry_domain_not_found" for error in errors)


def test_primary_entry_domain_must_be_root_domain():
    graph = make_valid_graph()

    graph["domains"].append(
        {
            "id": "domain_b",
            "name": "Domain B",
            "description": "Description of Domain B.",
            "learning_objective": "Learn Domain B.",
        }
    )

    graph["concepts"].extend(
        [
            {
                "id": "concept_c",
                "name": "Concept C",
                "description": "Description of Concept C.",
                "learning_objective": "Learn Concept C.",
            },
            {
                "id": "concept_d",
                "name": "Concept D",
                "description": "Description of Concept D.",
                "learning_objective": "Learn Concept D.",
            },
        ]
    )

    graph["relationships"].extend(
        [
            {
                "from": "domain_b",
                "to": "concept_c",
                "type": "contains",
            },
            {
                "from": "domain_b",
                "to": "concept_d",
                "type": "contains",
            },
            {
                "from": "domain_b",
                "to": "domain_a",
                "type": "prerequisite_for",
            },
        ]
    )

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "primary_entry_domain_not_root" for error in errors)


def test_invalid_graph_version_returns_error():
    graph = make_valid_graph()
    graph["graph_version"] = "version-two"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "invalid_graph_version" for error in errors)


def test_graph_without_domains_returns_error():
    graph = make_valid_graph()
    graph["domains"] = []

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "missing_domains" for error in errors)


def test_missing_concept_description_returns_error():
    graph = make_valid_graph()
    del graph["concepts"][0]["description"]

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "missing_concept_description" for error in errors)


def test_primary_entry_domain_must_be_domain():
    graph = make_valid_graph()
    graph["primary_entry_domain"] = "concept_a"

    errors = validate_learning_graph(graph)

    assert any(error["code"] == "primary_entry_domain_not_domain" for error in errors)
