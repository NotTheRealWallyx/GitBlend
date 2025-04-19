import subprocess

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    """Revert the last N commits."""
    num_commits = args.num_commits
    remote = args.remote

    # Revert the last N commits
    subprocess.run(
        [GIT_EXECUTABLE, "revert", f"HEAD~{num_commits}..HEAD"],
        text=True,
        check=True,
    )
    print(f"✅ Reverted the last {num_commits} commits.")

    # Push the changes to the remote if --push is specified
    if remote:
        subprocess.run([GIT_EXECUTABLE, "push"], text=True, check=True)
        print("✅ Changes pushed to the remote repository.")
