import pytest
class ConfigError(Exception):
    pass
def load_config(file_path):
    try:
        with open(file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise ConfigError("Config file not found")
def test_load_config_success(tmp_path):
    config_file = tmp_path / "config.txt"
    config_file.write_text("debug=true")
    result = load_config(config_file)
    assert result == "debug=true"
def test_load_config_missing_file():
    with pytest.raises(ConfigError):
        load_config("missing_config.txt")