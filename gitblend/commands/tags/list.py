import subprocess

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    """List all Git tags."""
    result = subprocess.run(
        [GIT_EXECUTABLE, "tag"], text=True, capture_output=True, check=True
    )
    tags = result.stdout.strip().split("\n")
    if tags and tags[0]:
        print("📋 Git Tags:")
        for tag in tags:
            print(tag)
    else:
        print("No tags found in the repository.")
