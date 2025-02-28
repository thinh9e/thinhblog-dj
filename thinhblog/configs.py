import tomllib
from pathlib import Path
from threading import Lock
from typing import Any


class Config:
    _instance = None
    _lock = Lock()

    _config_file = "configs.toml"
    _config_data = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._load()
        return cls._instance

    def _load(self):
        config_path = Path(self._config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"Not found config file: {config_path}")

        try:
            with config_path.open("rb") as file:
                self._config_data = tomllib.load(file)
        except tomllib.TOMLDecodeError as e:
            raise ValueError(f"Error parsing config file: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error while loading config: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        return self._config_data.get(key, default)


# Load configuration from file
config = Config()
