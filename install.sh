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
poetry build

# Check if poetry build was successful
if ! poetry build; then
  echo "Poetry build failed. Please ensure that poetry is set up correctly."
  exit 1
fi

if ! command -v pipx &> /dev/null; then
  echo "pipx is not installed. Installing pipx via Homebrew..."
  # Install and check if Homebrew installation succeeded
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

echo "Cleaning up..."
rm -rf $DIST_DIR

echo "Installation completed."
