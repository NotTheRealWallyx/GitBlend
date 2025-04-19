import subprocess

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    """Revert the last N commits."""
    num_commits = args.num_commits
    push = args.push

    subprocess.run(
        [GIT_EXECUTABLE, "revert", f"HEAD~{num_commits}..HEAD"],
        text=True,
        check=True,
    )
    print(f"✅ Reverted the last {num_commits} commits.")

    if push:
        subprocess.run([GIT_EXECUTABLE, "push"], text=True, check=True)
        print("✅ Changes pushed to the remote repository.")
