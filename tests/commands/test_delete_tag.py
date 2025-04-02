import pytest
from git import GitCommandError, InvalidGitRepositoryError
from gitblend.commands import delete_tag


@pytest.fixture
def mock_repo(mocker):
    """Mock the Repo object from GitPython."""
    return mocker.patch("gitblend.commands.delete_tag.Repo")


def test_delete_tag_success(mock_repo, mocker):
    """Test deleting a tag successfully."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.tags = ["v1.0.0"]
    mock_repo_instance.delete_tag = mocker.Mock()
    mock_repo_instance.git.push = mocker.Mock()

    args = type("Args", (object,), {"tag": "v1.0.0"})
    delete_tag.run(args)

    # Assert the local tag was deleted
    mock_repo_instance.delete_tag.assert_called_once_with("v1.0.0")
    # Assert the remote tag was deleted
    mock_repo_instance.git.push.assert_called_once_with("origin", ":refs/tags/v1.0.0")


def test_delete_tag_local_fail(mock_repo, mocker):
    """Test when the local tag does not exist."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.tags = []
    mock_repo_instance.delete_tag = mocker.Mock()

    args = type("Args", (object,), {"tag": "v1.0.0"})

    with pytest.raises(SystemExit) as e:
        delete_tag.run(args)

    assert e.value.code == 1
    mock_repo_instance.delete_tag.assert_not_called()


def test_delete_tag_remote_fail(mock_repo, mocker):
    """Test when deleting the remote tag fails."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.tags = ["v1.0.0"]
    mock_repo_instance.delete_tag = mocker.Mock()
    mock_repo_instance.git.push = mocker.Mock(
        side_effect=GitCommandError("push", "Error")
    )

    args = type("Args", (object,), {"tag": "v1.0.0"})

    with pytest.raises(SystemExit) as e:
        delete_tag.run(args)

    assert e.value.code == 1
    mock_repo_instance.delete_tag.assert_called_once_with("v1.0.0")
    mock_repo_instance.git.push.assert_called_once_with("origin", ":refs/tags/v1.0.0")


def test_invalid_git_repository(mocker):
    """Test when the current directory is not a valid Git repository."""
    mocker.patch(
        "gitblend.commands.delete_tag.Repo",
        side_effect=InvalidGitRepositoryError("Invalid repository"),
    )

    args = type("Args", (object,), {"tag": "v1.0.0"})

    with pytest.raises(SystemExit) as e:
        delete_tag.run(args)

    assert e.value.code == 1
