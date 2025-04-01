#!/bin/bash

# Step 1: Extract version from pyproject.toml
VERSION=$(grep '^version' pyproject.toml | awk -F= '{print $2}' | tr -d ' "')

if [ -z "$VERSION" ]; then
  echo "Error: Version not found in pyproject.toml"
  exit 1
fi

# Step 2: Define the package path
PACKAGE_NAME="gitblend"
PACKAGE_PATH="dist/$PACKAGE_NAME-$VERSION.tar.gz"
DIST_DIR="dist"

# Step 3: Build the package using Poetry
echo "Building the package using Poetry..."
poetry build

# Check if poetry build was successful
if [ $? -ne 0 ]; then
  echo "Poetry build failed. Please ensure that poetry is set up correctly."
  exit 1
fi

# Step 4: Check if pipx is installed
if ! command -v pipx &> /dev/null; then
  echo "pipx is not installed. Installing pipx via Homebrew..."
  brew install pipx

  # Check if Homebrew installation succeeded
  if [ $? -ne 0 ]; then
    echo "Failed to install pipx using Homebrew. Please install pipx manually and rerun the installer."
    exit 1
  fi
fi

# Step 5: Install the package using pipx
echo "Installing $PACKAGE_NAME version $VERSION with pipx..."

# Use pipx to install, pointing to the .tar.gz file
pipx install --force $PACKAGE_PATH

# Verify successful installation
if [ $? -eq 0 ]; then
  echo "$PACKAGE_NAME version $VERSION installed successfully with pipx."
else
  echo "Failed to install $PACKAGE_NAME version $VERSION with pipx."
  exit 1
fi

# Clean up (optional)
echo "Cleaning up..."
rm -rf $DIST_DIR

echo "Installation completed."
