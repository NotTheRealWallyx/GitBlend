import subprocess
import sys


def handle_git_errors(func):
    """Decorator to handle common Git errors."""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running git command: {e}", file=sys.stderr)
            raise SystemExit(e.returncode)

    return wrapper
