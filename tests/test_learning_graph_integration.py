from pathlib import Path

from src.learning_graph.loader import load_learning_graph
from src.learning_graph.validator import validate_learning_graph


def test_public_junior_data_analyst_graph_is_valid():
    project_root = Path(__file__).resolve().parents[1]

    graph_path = (
        project_root / "learning_graphs" / "junior_data_analyst_onboarding_v0_2.yaml"
    )

    graph = load_learning_graph(graph_path)
    errors = validate_learning_graph(graph)

    assert errors == []
