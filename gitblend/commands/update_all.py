import os
import subprocess

from gitblend.utils import handle_git_errors

GIT_EXECUTABLE = "/usr/bin/git"


def find_git_repos(start_path):
    """Recursively find all Git repositories starting from the given path."""
    git_repos = []
    for root, dirs in os.walk(start_path):
        if ".git" in dirs:
            git_repos.append(root)
            dirs.remove(".git")
    return git_repos


def is_dirty(repo_path):
    """Check if a Git repository has uncommitted changes."""
    result = subprocess.run(
        [GIT_EXECUTABLE, "status", "--porcelain"],
        cwd=repo_path,
        text=True,
        capture_output=True,
    )
    return bool(result.stdout.strip())


def stash_changes(repo_path):
    """Stash changes in a Git repository."""
    subprocess.run(
        [GIT_EXECUTABLE, "stash", "save", "Auto-stash before updating main"],
        cwd=repo_path,
        check=True,
    )


def switch_branch(repo_path, branch):
    """Switch to a specific branch in a Git repository."""
    subprocess.run([GIT_EXECUTABLE, "checkout", branch], cwd=repo_path, check=True)


def pull_changes(repo_path):
    """Pull the latest changes in the current branch of a Git repository."""
    subprocess.run([GIT_EXECUTABLE, "pull"], cwd=repo_path, check=True)


def has_stash(repo_path):
    """Check if there are stashed changes in a Git repository."""
    result = subprocess.run(
        [GIT_EXECUTABLE, "stash", "list"], cwd=repo_path, text=True, capture_output=True
    )
    return bool(result.stdout.strip())


def pop_stash(repo_path):
    """Pop the latest stash in a Git repository."""
    subprocess.run([GIT_EXECUTABLE, "stash", "pop"], cwd=repo_path, check=True)


@handle_git_errors
def run(args):
    """Update all Git repositories on the computer."""
    start_path = args.path or os.path.expanduser("~")
    only_clean = args.only_clean
    print(f"🔍 Searching for Git repositories in {start_path}...")

    git_repos = find_git_repos(start_path)

    if not git_repos:
        print("❌ No Git repositories found.")
        return

    print(f"✅ Found {len(git_repos)} repositories. Updating...")

    for repo_path in git_repos:
        try:
            print(f"🔄 Processing repository at {repo_path}...")

            result = subprocess.run(
                [GIT_EXECUTABLE, "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=repo_path,
                text=True,
                capture_output=True,
                check=True,
            )
            current_branch = result.stdout.strip()
            print(f"📍 Current branch: {current_branch}")

            if only_clean:
                if current_branch != "main" or is_dirty(repo_path):
                    print("⚠️ Skipping repository as it is not clean or not on main.")
                    continue

            if is_dirty(repo_path):
                print("⚠️ Uncommitted changes detected. Stashing...")
                stash_changes(repo_path)

            if current_branch != "main":
                print("🔄 Switching to main branch...")
                switch_branch(repo_path, "main")

            print("⬇️ Pulling latest changes on main...")
            pull_changes(repo_path)

            if current_branch != "main":
                print(f"🔄 Switching back to branch: {current_branch}...")
                switch_branch(repo_path, current_branch)

            if has_stash(repo_path):
                print("🔄 Unstashing changes...")
                pop_stash(repo_path)

            print(f"✅ Repository at {repo_path} updated successfully.")

        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to update repository at {repo_path}: {e}")
