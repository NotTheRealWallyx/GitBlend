import subprocess

from gitblend.utils import GIT_EXECUTABLE


def run(args):
    """Set a new URL for a Git remote."""
    subprocess.run(
        [GIT_EXECUTABLE, "remote", "set-url", args.remote, args.url],
        text=True,
        check=True,
    )
    print(f"\u2705 Remote '{args.remote}' URL set to: {args.url}")
