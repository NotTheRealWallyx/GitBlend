import subprocess
import sys


def run(args):
    tag_name = args.tag

    # Delete tag locally
    try:
        subprocess.run(["git", "tag", "-d", tag_name], check=True)
        print(f"✅ Tag '{tag_name}' deleted locally.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to delete local tag '{tag_name}'.")
        sys.exit(1)

    # Delete tag remotely
    try:
        subprocess.run(
            ["git", "push", "--delete", "origin", tag_name], check=True
        )
        print(f"✅ Tag '{tag_name}' deleted remotely.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to delete remote tag '{tag_name}'.")
        sys.exit(1)
