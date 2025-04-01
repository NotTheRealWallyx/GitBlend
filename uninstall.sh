#!/bin/bash

VERSION=$(grep '^version' pyproject.toml | awk -F= '{print $2}' | tr -d ' "')

if [ -z "$VERSION" ]; then
  echo "Error: Version not found in pyproject.toml"
  exit 1
fi

PACKAGE_NAME="gitblend"

if ! command -v pipx &> /dev/null; then
  echo "Error: pipx is not installed. Please install pipx and try again."
  exit 1
fi

echo "Uninstalling $PACKAGE_NAME version $VERSION with pipx..."

pipx uninstall $PACKAGE_NAME

# Verify successful uninstallation
if [ $? -eq 0 ]; then
  echo "$PACKAGE_NAME version $VERSION uninstalled successfully with pipx."
else
  echo "Failed to uninstall $PACKAGE_NAME version $VERSION with pipx."
  exit 1
fi

echo "Cleaning up residual build files..."

DIST_DIR="dist"
if [ -d "$DIST_DIR" ]; then
  rm -rf $DIST_DIR
  echo "Cleaned up residual build files."
else
  echo "No residual build files to clean up."
fi

echo "Uninstallation completed."
