# GitBlend

GitBlend is a Git utility tool that combines Git and GitHub commands to streamline your workflow. It provides a simple CLI interface for managing Git operations, such as deleting tags both locally and remotely.

## Features

- **Delete Git Tags**: Easily delete Git tags locally and remotely with a single command.
- **CLI Interface**: Simple and intuitive command-line interface for seamless usage.

## Installation

### Prerequisites

- Python 3.7 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- [pipx](https://pypa.github.io/pipx/) for isolated Python package installations

### Steps

1. Clone the repository:

```bash
git clone https://github.com/mikelsanchez/GitBlend.git
cd GitBlend
```

1. Run the installation script:

```bash
./install.sh
```

This script will:

- Build the package using Poetry.
- Install the package using pipx.

## Usage

After installation, you can use the `gitblend` command from your terminal.

### Delete a Git Tag

To delete a Git tag both locally and remotely, use the `delete-tag` command:

```bash
gitblend delete-tag <tag-name>
```

For example:

```bash
gitblend delete-tag v1.0.0
```

This will:

1. Delete the tag locally.
1. Delete the tag from the remote repository.

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
