import toml


def run(args):
    """Display the current version of GitBlend."""
    pyproject_path = "pyproject.toml"
    with open(pyproject_path, "r") as file:
        pyproject_data = toml.load(file)
    version = pyproject_data["tool"]["poetry"]["version"]
    print(f"GitBlend version {version}")
