import os
import shutil
import subprocess
import sys

CONFIG_DIR = os.path.expanduser("~/.config/gitblend")
REPO_PATH_FILE = os.path.join(CONFIG_DIR, "repo_path")


def get_repo_path():
    if not os.path.exists(REPO_PATH_FILE):
        return None
    with open(REPO_PATH_FILE) as f:
        return f.read().strip()


def run(args):
    repo_path = get_repo_path()
    if not repo_path:
        print(
            "❌ GitBlend repo path not configured. Reinstall using install.sh to enable self-update.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not os.path.isdir(repo_path):
        print(
            f"❌ Repo path '{repo_path}' no longer exists. Reinstall using install.sh.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"📂 Using repo at: {repo_path}")
    print("⬇️  Pulling latest changes...")
    try:
        subprocess.run(["git", "pull"], cwd=repo_path, check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to pull latest changes.", file=sys.stderr)
        sys.exit(1)

    print("🔨 Building package...")
    try:
        subprocess.run(["poetry", "build"], cwd=repo_path, check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to build package.", file=sys.stderr)
        sys.exit(1)

    dist_dir = os.path.join(repo_path, "dist")
    tarballs = sorted(f for f in os.listdir(dist_dir) if f.endswith(".tar.gz"))
    if not tarballs:
        print("❌ No built package found in dist/.", file=sys.stderr)
        sys.exit(1)
    package_path = os.path.join(dist_dir, tarballs[-1])

    print("📦 Reinstalling with pipx...")
    try:
        subprocess.run(["pipx", "install", "--force", package_path], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to reinstall with pipx.", file=sys.stderr)
        sys.exit(1)

    shutil.rmtree(dist_dir, ignore_errors=True)
    print("✅ GitBlend updated successfully!")
