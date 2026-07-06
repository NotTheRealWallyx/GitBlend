import os

import toml

from gitblend.config import CONFIG_PATH


def prompt_yes_no(question):
    """Ask a yes/no question and return the answer as a boolean."""
    answer = input(f"{question} [y/N]: ").strip().lower()
    return answer in ("y", "yes")


def run(args):
    """Interactively generate the GitBlend configuration file."""
    if os.path.exists(CONFIG_PATH) and not args.force:
        if not prompt_yes_no(f"⚠️ {CONFIG_PATH} already exists. Overwrite it?"):
            print("Setup cancelled. Existing configuration left untouched.")
            return

    config = {
        "commit": {
            "add": prompt_yes_no(
                "Always stage all files before committing (same as --add)?"
            ),
            "sign": prompt_yes_no(
                "Always sign commits with your GPG key (same as --sign)?"
            ),
            "allow_empty": prompt_yes_no(
                "Always allow empty commits (same as --allow-empty)?"
            ),
        }
    }

    with open(CONFIG_PATH, "w") as file:
        toml.dump(config, file)

    print(f"✅ Configuration written to {CONFIG_PATH}")
