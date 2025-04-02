import subprocess
import sys


def run(args):
    """List all Git tags."""
    try:
        result = subprocess.run(
            ["git", "tag"], check=True, text=True, capture_output=True
        )
        tags = result.stdout.strip()
        if tags:
            print("📋 Git Tags:")
            print(tags)
        else:
            print("No tags found in the repository.")
    except subprocess.CalledProcessError:
        print("❌ Failed to list Git tags.")
        sys.exit(1)
