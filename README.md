# GitBlend

[![Run pytest](https://github.com/NotTheRealWallyx/GitBlend/actions/workflows/check_test.yml/badge.svg)](https://github.com/NotTheRealWallyx/GitBlend/actions/workflows/ci_entrypoint.yml) [![CodeFactor](https://www.codefactor.io/repository/github/nottherealwallyx/gitblend/badge)](https://www.codefactor.io/repository/github/nottherealwallyx/gitblend)

![GitBlend image](assets/images/gitblend_image.png)

GitBlend is a Git utility tool that combines Git and GitHub commands to streamline your workflow. It provides a simple CLI interface for managing Git operations, such as deleting tags both locally and remotely.

## Features

GitBlend is a versatile tool designed to simplify your Git and GitHub workflows. Here are some of the key features:

- **Tag Management**: Manage Git tags effortlessly with commands to create, delete, rename, and list tags. Whether you need to annotate a release, clean up old tags, or rename an existing tag, GitBlend provides a streamlined interface for these operations.

  - Create annotated tags with custom messages.
  - Push tags to remote repositories.
  - Delete tags both locally and remotely.
  - Rename tags while preserving their history.
  - List all tags in your repository.

- **Repository Management**: Keep your repositories up-to-date with the `update-all` command. This command:

  - Recursively finds all Git repositories on your computer.
  - Updates repositories to the latest changes on the `main` branch.
  - Optionally skips repositories with uncommitted changes or those not on the `main` branch.

- **Commit Management**: Simplify the process of creating commits with the `create-commit` command. This includes:
  - Adding all files to the commit with the `--add` flag.
  - Creating commits even when there are no changes using the `--allow-empty` flag.

- **General Commands**: Access helpful utilities like:
  - Displaying the current version of GitBlend.
  - Viewing detailed help for all available commands.

## Installation

### Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- [pipx](https://pypa.github.io/pipx/) for isolated Python package installations

### Steps

1. Clone the repository:

```bash
git clone https://github.com/mikelsanchez/GitBlend.git
cd GitBlend
```

2. Run the installation script:

```bash
./install.sh
```

This script will:

- Build the package using Poetry.
- Install the package using pipx.

## Usage

After installation, you can use the `gitblend` command from your terminal, followed by the desired command.

### Available Commands

#### Tag Management

- `gitblend list-tags`: List all Git tags in the current repository.
- `gitblend create-tag <tag_name> --message "<tag_message>" [--push]`: Create a new Git tag with an optional push to the remote repository.
- `gitblend delete-tag <tag_name>`: Delete a Git tag both locally and remotely.
- `gitblend rename-tag <old_tag> <new_tag>`: Rename an existing Git tag both locally and remotely.

#### Repository Management

- `gitblend update-all [--path <path>] [--only-clean]`: Update all Git repositories on your computer. Use `--only-clean` to skip repositories that are not on the `main` branch or have uncommitted changes.

#### Commit Management

- `gitblend create-commit --message "<commit_message>" [--add]`: Create a new Git commit with a message. Use `--add` to stage all files before committing.

#### General

- `gitblend --help`: Show help information for the GitBlend CLI.

## Uninstallation

To uninstall GitBlend, run the uninstallation script:

```bash
./uninstall.sh
```

This script will:

1. Uninstall the package using pipx.
1. Clean up any residual build files.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
