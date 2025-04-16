import pytest
from git import GitCommandError

from gitblend.commands import create_tag


@pytest.fixture
def mock_repo(mocker):
    """Mock the Repo object from GitPython."""
    return mocker.patch("gitblend.commands.create_tag.Repo")


def test_create_tag_success(mock_repo, mocker):
    """Test creating a tag successfully."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.create_tag = mocker.Mock()
    mock_repo_instance.git.push = mocker.Mock()

    args = type(
        "Args",
        (object,),
        {"tag": "v1.0.0", "message": "Initial release", "push": False},
    )
    create_tag.run(args)

    mock_repo_instance.create_tag.assert_called_once_with(
        "v1.0.0", message="Initial release"
    )
    mock_repo_instance.git.push.assert_not_called()


def test_create_tag_with_push(mock_repo, mocker):
    """Test creating a tag and pushing it to the remote repository."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.create_tag = mocker.Mock()
    mock_repo_instance.git.push = mocker.Mock()

    args = type(
        "Args",
        (object,),
        {"tag": "v1.0.0", "message": "Initial release", "push": True},
    )
    create_tag.run(args)

    mock_repo_instance.create_tag.assert_called_once_with(
        "v1.0.0", message="Initial release"
    )
    mock_repo_instance.git.push.assert_called_once_with("origin", "v1.0.0")


def test_create_tag_failure(mock_repo):
    """Test failure when creating a tag."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.create_tag.side_effect = GitCommandError("git tag", "Error")

    args = type(
        "Args",
        (object,),
        {"tag": "v1.0.0", "message": "Initial release", "push": False},
    )

    with pytest.raises(SystemExit) as e:
        create_tag.run(args)

    assert e.value.code == 1
    mock_repo_instance.create_tag.assert_called_once_with(
        "v1.0.0", message="Initial release"
    )


def test_push_tag_failure(mock_repo, mocker):
    """Test failure when pushing a tag to the remote repository."""
    mock_repo_instance = mock_repo.return_value
    mock_repo_instance.create_tag = mocker.Mock()
    mock_repo_instance.git.push.side_effect = GitCommandError("git push", "Error")

    args = type(
        "Args",
        (object,),
        {"tag": "v1.0.0", "message": "Initial release", "push": True},
    )

    with pytest.raises(SystemExit) as e:
        create_tag.run(args)

    assert e.value.code == 1
    mock_repo_instance.create_tag.assert_called_once_with(
        "v1.0.0", message="Initial release"
    )
    mock_repo_instance.git.push.assert_called_once_with("origin", "v1.0.0")
