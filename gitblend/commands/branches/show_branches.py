import subprocess

from gitblend.utils import GIT_EXECUTABLE


def run(args):
    """Show all local Git branches."""
    result = subprocess.run(
        [GIT_EXECUTABLE, "branch"], text=True, capture_output=True, check=True
    )
    print("\U0001f33f Local branches:")
    print(result.stdout.strip())
