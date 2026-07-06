#!/bin/bash

VERSION=$(grep '^version' pyproject.toml | awk -F= '{print $2}' | tr -d ' "')

if [ -z "$VERSION" ]; then
  echo "Error: Version not found in pyproject.toml"
  exit 1
fi

PACKAGE_NAME="gitblend"
PACKAGE_PATH="dist/$PACKAGE_NAME-$VERSION.tar.gz"
DIST_DIR="dist"

echo "Building the package using Poetry..."
if ! poetry build; then
  echo "Poetry build failed. Please ensure that poetry is set up correctly."
  exit 1
fi

if ! command -v pipx &> /dev/null; then
  echo "pipx is not installed. Installing pipx via Homebrew..."
  if ! brew install pipx; then
    echo "Failed to install pipx using Homebrew. Please install pipx manually and rerun the installer."
    exit 1
  fi
fi

echo "Installing $PACKAGE_NAME version $VERSION with pipx..."
if pipx install --force $PACKAGE_PATH; then
  echo "$PACKAGE_NAME version $VERSION installed successfully with pipx."
else
  echo "Failed to install $PACKAGE_NAME version $VERSION with pipx."
  exit 1
fi

echo "Saving repo path for self-update..."
GITBLEND_CONFIG_DIR="$HOME/.config/gitblend"
mkdir -p "$GITBLEND_CONFIG_DIR"
pwd > "$GITBLEND_CONFIG_DIR/repo_path"
echo "Repo path saved to $GITBLEND_CONFIG_DIR/repo_path"

echo "Cleaning up..."
rm -rf $DIST_DIR

if [ ! -f "$HOME/.gitblend.toml" ] && [ -t 0 ]; then
  read -r -p "No GitBlend configuration found. Create one now? [y/N]: " CREATE_CONFIG
  case "$CREATE_CONFIG" in
    [yY]|[yY][eE][sS]) gib setup ;;
    *) echo "You can create it later by running 'gib setup'." ;;
  esac
fi

echo "Installation completed."
