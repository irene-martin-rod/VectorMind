
from pathlib import Path

import yaml


def get_project_root() -> Path:
    '''
    Get the root directory of the VectorMind project.

    Parameters:
        - None

    Returns:
        - Path : absolute path to the project root directory.
    '''
    return Path(__file__).resolve().parents[2]


def load_config(config_path: str | Path) -> dict:
    '''
    Load a YAML configuration file.

    Parameters:
        - config_path : path to the YAML configuration file.

    Returns:
        - config : dictionary containing the configuration parameters.

    Raises:
        - FileNotFoundError : if the configuration file does not exist.
        - ValueError : if the configuration file is empty.
    '''
    config_path = Path(config_path)

    if not config_path.is_absolute():
        config_path = get_project_root() / config_path

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise ValueError(
            f"Configuration file is empty: {config_path}"
        )

    return config


def validate_config(config: dict) -> None:
    '''
    Validate the structure and values of a configuration dictionary.

    Parameters:
        - config : dictionary containing the configuration parameters.

    Returns:
        - None : if the configuration is valid.

    Raises:
        - TypeError : if a configuration section has an invalid type.
        - ValueError : if a required field is missing or has an invalid value.
    '''
    if not isinstance(config, dict):
        raise TypeError("Configuration must be a dictionary.")

    required_sections = ["dataset", "retrieval", "models"]

    for section in required_sections:
        if section not in config:
            raise ValueError(
                f"Missing required configuration section: {section}"
            )

    dataset = config["dataset"]
    retrieval = config["retrieval"]
    models = config["models"]

    if not isinstance(dataset, dict):
        raise TypeError("'dataset' must be a dictionary.")

    if not isinstance(retrieval, dict):
        raise TypeError("'retrieval' must be a dictionary.")

    if not isinstance(models, dict):
        raise TypeError("'models' must be a dictionary.")

    if not isinstance(dataset.get("name"), str) or not dataset["name"].strip():
        raise ValueError("'dataset.name' must be a non-empty string.")

    if not isinstance(dataset.get("split"), str) or not dataset["split"].strip():
        raise ValueError("'dataset.split' must be a non-empty string.")

    top_k = retrieval.get("top_k")

    if type(top_k) is not int or top_k <= 0:
        raise ValueError("'retrieval.top_k' must be a positive integer.")

    dense_model = models.get("dense")

    if not isinstance(dense_model, dict):
        raise TypeError("'models.dense' must be a dictionary.")

    if (
        not isinstance(dense_model.get("name"), str)
        or not dense_model["name"].strip()
    ):
        raise ValueError("'models.dense.name' must be a non-empty string.")

    if type(dense_model.get("normalize_embeddings")) is not bool:
        raise ValueError(
            "'models.dense.normalize_embeddings' must be a boolean."
        )
