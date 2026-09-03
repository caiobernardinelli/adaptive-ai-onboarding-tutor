import pytest
import yaml

from src.learning_graph.loader import load_learning_graph


def test_load_valid_yaml(tmp_path):
    yaml_file = tmp_path / "valid.yaml"
    yaml_file.write_text(
        "graph_id: test_graph\ngraph_version: '0.1'\n",
        encoding="utf-8",
    )

    result = load_learning_graph(yaml_file)

    assert result == {
        "graph_id": "test_graph",
        "graph_version": "0.1",
    }


def test_load_missing_file_raises_file_not_found(tmp_path):
    missing_file = tmp_path / "missing.yaml"

    with pytest.raises(FileNotFoundError):
        load_learning_graph(missing_file)


def test_load_malformed_yaml_raises_yaml_error(tmp_path):
    malformed_file = tmp_path / "malformed.yaml"

    malformed_file.write_text(
        "graph_id: [invalid_yaml\n",
        encoding="utf-8",
    )

    with pytest.raises(yaml.YAMLError):
        load_learning_graph(malformed_file)


def test_load_empty_yaml_returns_none(tmp_path):
    empty_file = tmp_path / "empty.yaml"

    empty_file.write_text("", encoding="utf-8")

    result = load_learning_graph(empty_file)

    assert result is None
