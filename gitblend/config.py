import os
import sys

import toml

CONFIG_PATH = os.path.expanduser("~/.gitblend.toml")


def load_config():
    """Load the user configuration from ~/.gitblend.toml, if it exists."""
    try:
        with open(CONFIG_PATH, "r") as file:
            return toml.load(file)
    except FileNotFoundError:
        return {}
    except toml.TomlDecodeError as e:
        print(f"⚠️ Ignoring invalid config file {CONFIG_PATH}: {e}", file=sys.stderr)
        return {}
