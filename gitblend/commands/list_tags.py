from git import Repo

from gitblend.utils import handle_git_errors


@handle_git_errors
def run(args):
    """List all Git tags."""
    repo = Repo(search_parent_directories=True)

    # Get all tags
    tags = repo.tags
    if tags:
        print("📋 Git Tags:")
        for tag in tags:
            print(tag.name)
    else:
        print("No tags found in the repository.")
