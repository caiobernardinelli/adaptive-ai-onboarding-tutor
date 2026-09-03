import yaml


def load_learning_graph(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        schema = yaml.safe_load(file)

    return schema
