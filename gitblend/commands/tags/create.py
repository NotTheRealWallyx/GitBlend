import subprocess

from gitblend.utils import handle_git_errors


@handle_git_errors
def run(args):
    """Create a new Git tag."""
    tag_name = args.tag
    message = args.message
    push = args.push

    subprocess.run(["git", "tag", "-a", tag_name, "-m", message], text=True, check=True)
    print(f"✅ Tag '{tag_name}' created successfully.")

    # Push the tag if requested
    if push:
        subprocess.run(["git", "push", "origin", tag_name], text=True, check=True)
        print(f"✅ Tag '{tag_name}' pushed to remote repository.")
