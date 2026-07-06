import subprocess
import sys

from gitblend.utils import GIT_EXECUTABLE, handle_git_errors


@handle_git_errors
def run(args):
    """Create a new Git commit with a message."""
    message = args.message or getattr(args, "positional_message", None)
    if not message:
        print(
            "❌ A commit message is required (pass it as an argument or with -m).",
            file=sys.stderr,
        )
        raise SystemExit(2)

    if args.add:
        subprocess.run([GIT_EXECUTABLE, "add", "."], text=True, check=True)
        print("✅ All files added to the commit.")

    commit_command = [GIT_EXECUTABLE, "commit", "--allow-empty", "-m", message]

    if args.sign:
        commit_command.append("--gpg-sign")

    subprocess.run(commit_command, text=True, check=True)
    print(f"✅ Commit created successfully with message: '{message}'")
