import subprocess

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    """Create a new Git commit with a message."""
    message = args.message
    subprocess.run([GIT_EXECUTABLE, "commit", "-m", message], text=True, check=True)
    print(f"✅ Commit created successfully with message: '{message}'")
