import pytest
import subprocess
from gitblend.commands import delete_tag


# Mock subprocess.run so we don't actually run git commands
@pytest.fixture
def mock_subprocess_run(mocker):
    return mocker.patch("subprocess.run")


def test_delete_tag_success(mock_subprocess_run):
    """Test deleting a tag successfully."""
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=[], returncode=0
    )

    args = type("Args", (object,), {"tag": "v1.0.0"})
    delete_tag.run(args)

    mock_subprocess_run.assert_any_call(
        ["git", "tag", "-d", "v1.0.0"], check=True
    )
    mock_subprocess_run.assert_any_call(
        ["git", "push", "--delete", "origin", "v1.0.0"], check=True
    )


def test_delete_tag_local_fail(mocker):
    """Test when deleting the local tag fails."""
    mocker.patch(
        "subprocess.run",
        side_effect=[subprocess.CalledProcessError(1, "git tag -d")],
    )

    args = type("Args", (object,), {"tag": "v1.0.0"})

    with pytest.raises(SystemExit) as e:
        delete_tag.run(args)

    assert e.value.code == 1


def test_delete_tag_remote_fail(mocker):
    """Test when deleting the remote tag fails."""
    mocker.patch(
        "subprocess.run",
        side_effect=[
            subprocess.CompletedProcess(args=[], returncode=0),
            subprocess.CalledProcessError(1, "git push --delete origin"),
        ],
    )

    args = type("Args", (object,), {"tag": "v1.0.0"})

    with pytest.raises(SystemExit) as e:
        delete_tag.run(args)

    assert e.value.code == 1
