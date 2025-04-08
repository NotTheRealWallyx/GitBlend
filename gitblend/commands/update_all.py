import os
from git import Repo, InvalidGitRepositoryError
from gitblend.utils import handle_git_errors


def find_git_repos(start_path):
    """Recursively find all Git repositories starting from the given path."""
    git_repos = []
    for root, dirs, files in os.walk(start_path):
        if ".git" in dirs:
            git_repos.append(root)
            dirs.remove(".git")
    return git_repos


@handle_git_errors
def run(args):
    """Update all Git repositories on the computer."""
    start_path = args.path or os.path.expanduser("~")  # Ensure default path is set
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
            repo = Repo(repo_path)

            current_branch = repo.active_branch.name
            print(f"📍 Current branch: {current_branch}")

            if only_clean:
                if current_branch != "main" or repo.is_dirty():
                    print("⚠️ Skipping repository as it is not clean or not on main.")
                    continue

            if repo.is_dirty():
                print("⚠️ Uncommitted changes detected. Stashing...")
                repo.git.stash("save", "Auto-stash before updating main")

            if current_branch != "main":
                print("🔄 Switching to main branch...")
                repo.git.checkout("main")

            print("⬇️ Pulling latest changes on main...")
            repo.git.pull()

            if current_branch != "main":
                print(f"🔄 Switching back to branch: {current_branch}...")
                repo.git.checkout(current_branch)

            if repo.git.stash("list"):
                print("🔄 Unstashing changes...")
                repo.git.stash("pop")

            print(f"✅ Repository at {repo_path} updated successfully.")

        except InvalidGitRepositoryError:
            print(f"❌ {repo_path} is not a valid Git repository. Skipping.")
        except Exception as e:
            print(f"❌ Failed to update repository at {repo_path}: {e}")
