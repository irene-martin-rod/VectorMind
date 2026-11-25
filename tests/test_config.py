
import pytest

from vectormind.config import (
    get_project_root,
    load_config,
    validate_config,
)


def test_get_project_root():
    '''
    Test retrieving the project root directory.

    Parameters:
        - None

    Returns:
        - None : asserts that the project root is correctly identified.
    '''
    project_root = get_project_root()

    assert project_root.is_absolute()
    assert (project_root / "pyproject.toml").exists()
    assert (project_root / "configs" / "baseline.yaml").exists()


def test_load_config_from_different_directory(monkeypatch, tmp_path):
    '''
    Test loading a configuration file from another working directory.

    Parameters:
        - monkeypatch : fixture used to temporarily modify the working directory.
        - tmp_path : fixture providing a temporary directory.

    Returns:
        - None : asserts that configuration loading works independently
          of the current working directory.
    '''
    monkeypatch.chdir(tmp_path)

    config = load_config("configs/baseline.yaml")

    assert config["dataset"]["name"] == "scifact"


def test_load_config():
    '''
    Test loading a YAML configuration file.

    Parameters:
        - None

    Returns:
        - None : asserts that the configuration is loaded as a dictionary.
    '''
    config = load_config("configs/baseline.yaml")

    assert isinstance(config, dict)


def test_load_empty_config(tmp_path):
    '''
    Test loading an empty YAML configuration file.

    Parameters:
        - tmp_path : fixture providing a temporary directory.

    Returns:
        - None : asserts that an empty configuration raises ValueError.
    '''
    empty_config = tmp_path / "empty.yaml"
    empty_config.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="empty"):
        load_config(empty_config)


def test_validate_config():
    '''
    Test validation of a valid configuration.

    Parameters:
        - None

    Returns:
        - None : asserts that the configuration passes validation.
    '''
    config = load_config("configs/baseline.yaml")

    assert validate_config(config) is None


def test_validate_config_invalid_top_k():
    '''
    Test validation with an invalid top_k value.

    Parameters:
        - None

    Returns:
        - None : asserts that invalid configuration raises ValueError.
    '''
    config = load_config("configs/baseline.yaml")
    config["retrieval"]["top_k"] = -10

    with pytest.raises(ValueError, match="retrieval.top_k"):
        validate_config(config)
