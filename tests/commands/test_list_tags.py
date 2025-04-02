import pytest
from git import InvalidGitRepositoryError, GitCommandError
from gitblend.commands import list_tags


@pytest.fixture
def mock_repo(mocker):
    """Mock the Repo object from GitPython."""
    return mocker.patch("gitblend.commands.list_tags.Repo")


def test_list_tags_success(mock_repo):
    """Test listing tags successfully."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.tags = [
        type("Tag", (object,), {"name": "v1.0.0"}),
        type("Tag", (object,), {"name": "v2.0.0"}),
    ]

    args = type("Args", (object,), {})
    list_tags.run(args)

    # No exceptions should be raised, and tags should be printed
    mock_repo.assert_called_once_with(search_parent_directories=True)


def test_list_tags_no_tags(mock_repo):
    """Test listing tags when no tags exist."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.tags = []

    args = type("Args", (object,), {})
    list_tags.run(args)

    # No exceptions should be raised, and no tags should be printed
    mock_repo.assert_called_once_with(search_parent_directories=True)


def test_list_tags_invalid_repo(mock_repo):
    """Test when the current directory is not a valid Git repository."""
    mock_repo.side_effect = InvalidGitRepositoryError("Invalid repository")

    args = type("Args", (object,), {})

    with pytest.raises(SystemExit) as e:
        list_tags.run(args)

    assert e.value.code == 1


def test_list_tags_git_command_error(mock_repo):
    """Test when a Git command error occurs."""
    mock_repo.side_effect = GitCommandError("git tag", "Error")

    args = type("Args", (object,), {})

    with pytest.raises(SystemExit) as e:
        list_tags.run(args)

    assert e.value.code == 1
