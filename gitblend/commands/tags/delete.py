import subprocess
import sys

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    tag_name = args.tag

    # Delete tag locally
    try:
        subprocess.run([GIT_EXECUTABLE, "tag", "-d", tag_name], text=True, check=True)
        print(f"✅ Tag '{tag_name}' deleted locally.")
    except subprocess.CalledProcessError:
        print(f"❌ Tag '{tag_name}' does not exist locally.", file=sys.stderr)
        sys.exit(1)

    # Delete tag remotely
    try:
        subprocess.run(
            [GIT_EXECUTABLE, "push", "origin", f":refs/tags/{tag_name}"],
            text=True,
            check=True,
        )
        print(f"✅ Tag '{tag_name}' deleted remotely.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to delete remote tag '{tag_name}'.", file=sys.stderr)
        sys.exit(1)
