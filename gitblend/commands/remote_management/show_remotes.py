import subprocess

from gitblend.utils import GIT_EXECUTABLE


def run(args):
    """Show all Git remotes."""
    result = subprocess.run(
        [GIT_EXECUTABLE, "remote", "-v"], text=True, capture_output=True, check=True
    )
    print("\U0001f4e1 Git remotes:")
    print(result.stdout.strip())
