CREATE TABLE learners (
    id TEXT PRIMARY KEY NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE enrollments (
    id TEXT PRIMARY KEY NOT NULL,
    learner_id TEXT NOT NULL,
    graph_id TEXT NOT NULL,
    graph_version TEXT NOT NULL,
    status TEXT NOT NULL
        CHECK (status IN ('active', 'completed')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    completed_at TEXT,

    FOREIGN KEY (learner_id)
        REFERENCES learners(id),

    CHECK (
        (status = 'active' AND completed_at IS NULL)
        OR
        (status = 'completed' AND completed_at IS NOT NULL)
    )
);

CREATE UNIQUE INDEX ux_enrollments_one_active_per_graph_version
ON enrollments (
    learner_id,
    graph_id,
    graph_version
)
WHERE status = 'active';

CREATE TABLE learner_progress (
    enrollment_id TEXT PRIMARY KEY NOT NULL,
    active_domain_id TEXT NOT NULL,
    active_concept_id TEXT,

    FOREIGN KEY (enrollment_id)
        REFERENCES enrollments(id)
);