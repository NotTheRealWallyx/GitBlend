import sys
from git import InvalidGitRepositoryError, GitCommandError


def handle_git_errors(func):
    """Decorator to handle common Git errors."""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidGitRepositoryError:
            print("❌ Error: Not inside a valid Git repository.", file=sys.stderr)
            sys.exit(1)
        except GitCommandError as e:
            print(f"❌ Git command error: {e}", file=sys.stderr)
            sys.exit(1)

    return wrapper
