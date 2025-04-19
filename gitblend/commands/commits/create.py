import subprocess

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    """Create a new Git commit with a message."""
    if args.add:
        subprocess.run([GIT_EXECUTABLE, "add", "."], text=True, check=True)
        print("✅ All files added to the commit.")

    message = args.message
    commit_command = [GIT_EXECUTABLE, "commit", "--allow-empty", "-m", message]

    if args.sign:
        commit_command.append("--gpg-sign")

    subprocess.run(commit_command, text=True, check=True)
    print(f"✅ Commit created successfully with message: '{message}'")
