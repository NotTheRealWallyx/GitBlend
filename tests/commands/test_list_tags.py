import pytest
import subprocess
from gitblend.commands import list_tags


@pytest.fixture
def mock_subprocess_run(mocker):
    return mocker.patch("subprocess.run")


def test_list_tags_success(mock_subprocess_run):
    """Test listing tags successfully."""
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=[], returncode=0, stdout="v1.0.0\nv2.0.0\n"
    )

    args = type("Args", (object,), {})
    list_tags.run(args)

    mock_subprocess_run.assert_called_once_with(
        ["git", "tag"], check=True, text=True, capture_output=True
    )


def test_list_tags_no_tags(mock_subprocess_run):
    """Test listing tags when no tags exist."""
    mock_subprocess_run.return_value = subprocess.CompletedProcess(
        args=[], returncode=0, stdout=""
    )

    args = type("Args", (object,), {})
    list_tags.run(args)

    mock_subprocess_run.assert_called_once_with(
        ["git", "tag"], check=True, text=True, capture_output=True
    )


def test_list_tags_failure(mock_subprocess_run):
    """Test failure when listing tags."""
    mock_subprocess_run.side_effect = subprocess.CalledProcessError(1, "git tag")

    args = type("Args", (object,), {})

    with pytest.raises(SystemExit) as e:
        list_tags.run(args)

    assert e.value.code == 1
