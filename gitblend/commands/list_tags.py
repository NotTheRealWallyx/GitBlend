import sys
from git import Repo, InvalidGitRepositoryError, GitCommandError


def run(args):
    """List all Git tags."""
    try:
        repo = Repo(search_parent_directories=True)

        # Get all tags
        tags = repo.tags
        if tags:
            print("📋 Git Tags:")
            for tag in tags:
                print(tag.name)
        else:
            print("No tags found in the repository.")

    except InvalidGitRepositoryError:
        print("❌ Error: Not inside a valid Git repository.", file=sys.stderr)
        sys.exit(1)

    except GitCommandError as e:
        print(f"❌ Git command error: {e}", file=sys.stderr)
        sys.exit(1)
