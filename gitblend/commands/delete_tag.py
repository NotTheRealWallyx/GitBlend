import sys
from git import Repo, GitCommandError, InvalidGitRepositoryError


def run(args):
    tag_name = args.tag

    try:
        repo = Repo(search_parent_directories=True)

        # Delete tag locally
        if tag_name in repo.tags:
            repo.delete_tag(tag_name)
            print(f"✅ Tag '{tag_name}' deleted locally.")
        else:
            print(f"❌ Tag '{tag_name}' does not exist locally.")
            sys.exit(1)

        # Delete tag remotely
        try:
            repo.git.push("origin", f":refs/tags/{tag_name}")
            print(f"✅ Tag '{tag_name}' deleted remotely.")
        except GitCommandError:
            print(f"❌ Failed to delete remote tag '{tag_name}'.")
            sys.exit(1)

    except GitCommandError as e:
        print(f"❌ Git command error: {e}")
        sys.exit(1)

    except InvalidGitRepositoryError:
        print("❌ Error: Not inside a valid Git repository.", file=sys.stderr)
        sys.exit(1)
