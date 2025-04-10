# GitBlend

[![Run pytest](https://github.com/NotTheRealWallyx/GitBlend/actions/workflows/check_test.yml/badge.svg)](https://github.com/NotTheRealWallyx/GitBlend/actions/workflows/ci_entrypoint.yml) [![CodeFactor](https://www.codefactor.io/repository/github/nottherealwallyx/gitblend/badge)](https://www.codefactor.io/repository/github/nottherealwallyx/gitblend)

![GitBlend image](assets/images/gitblend_image.png)

GitBlend is a Git utility tool that combines Git and GitHub commands to streamline your workflow. It provides a simple CLI interface for managing Git operations, such as deleting tags both locally and remotely.

## Features

- **Delete Git Tags**: Easily delete Git tags locally and remotely with a single command.
- **CLI Interface**: Simple and intuitive command-line interface for seamless usage.

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

- `gitblend list-tags`: List all Git tags in the current repository.
- `gitblend create-tag <tag_name> --message "<tag_message>" [--push]`: Create a new Git tag with an optional push to the remote repository.
- `gitblend delete-tag <tag_name>`: Delete a Git tag both locally and remotely.
- `gitblend rename-tag <old_tag> <new_tag>`: Rename an existing Git tag both locally and remotely.
- `gitblend update-all [--path <path>] [--only-clean]`: Update all Git repositories on your computer. Use `--only-clean` to skip repositories that are not on the `main` branch or have uncommitted changes.
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
