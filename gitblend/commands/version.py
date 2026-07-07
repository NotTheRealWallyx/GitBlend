from importlib.metadata import version as get_version


def run(args):
    """Display the current version of GitBlend."""
    print(f"GitBlend version {get_version('gitblend')}")
