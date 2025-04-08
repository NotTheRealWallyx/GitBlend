import os
from git import Repo, InvalidGitRepositoryError
from gitblend.utils import handle_git_errors


def find_git_repos(start_path):
    """Recursively find all Git repositories starting from the given path."""
    git_repos = []
    for root, dirs, files in os.walk(start_path):
        if ".git" in dirs:
            git_repos.append(root)
            dirs.remove(".git")  # Skip traversing into .git directories
    return git_repos


@handle_git_errors
def run(args):
    """Update all Git repositories on the computer."""
    start_path = args.path or os.path.expanduser("~")  # Ensure default path is set
    print(f"🔍 Searching for Git repositories in {start_path}...")

    git_repos = find_git_repos(start_path)

    if not git_repos:
        print("❌ No Git repositories found.")
        return

    print(f"✅ Found {len(git_repos)} repositories. Updating...")

    for repo_path in git_repos:
        try:
            print(f"🔄 Updating repository at {repo_path}...")
            repo = Repo(repo_path)
            if repo.is_dirty():
                print(f"⚠️ Repository at {repo_path} has uncommitted changes. Skipping.")
                continue
            repo.git.pull()
            print(f"✅ Repository at {repo_path} updated successfully.")
        except InvalidGitRepositoryError:
            print(f"❌ {repo_path} is not a valid Git repository. Skipping.")
        except Exception as e:
            print(f"❌ Failed to update repository at {repo_path}: {e}")
