import os
from unittest.mock import MagicMock, patch

import pytest

from gitblend.commands import update_all


def test_find_git_repos(tmp_path):
    """Test finding Git repositories in a directory."""
    # Create mock Git repositories
    repo1 = tmp_path / "repo1/.git"
    repo2 = tmp_path / "repo2/.git"
    repo1.mkdir(parents=True)
    repo2.mkdir(parents=True)

    repos = update_all.find_git_repos(tmp_path)

    assert len(repos) == 2
    assert str(tmp_path / "repo1") in repos
    assert str(tmp_path / "repo2") in repos


@patch("gitblend.commands.update_all.Repo")
def test_run_only_clean(mock_repo):
    """Test the --only-clean flag behavior."""
    # Mock repository behavior
    repo_mock = MagicMock()
    repo_mock.active_branch.name = "main"
    repo_mock.is_dirty.return_value = False
    mock_repo.return_value = repo_mock

    args = MagicMock()
    args.path = None
    args.only_clean = True

    with patch(
        "gitblend.commands.update_all.find_git_repos", return_value=["/mock/repo"]
    ):
        update_all.run(args)

    # Ensure pull is called since the repo is clean and on main
    repo_mock.git.pull.assert_called_once()


@patch("gitblend.commands.update_all.Repo")
def test_run_skip_dirty_or_not_main(mock_repo):
    """Test skipping repositories with --only-clean when dirty or not on main."""
    # Mock repository behavior
    repo_mock = MagicMock()
    repo_mock.active_branch.name = "feature-branch"
    repo_mock.is_dirty.return_value = True
    mock_repo.return_value = repo_mock

    args = MagicMock()
    args.path = None
    args.only_clean = True

    with patch(
        "gitblend.commands.update_all.find_git_repos", return_value=["/mock/repo"]
    ):
        update_all.run(args)

    # Ensure pull is not called since the repo is dirty and not on main
    repo_mock.git.pull.assert_not_called()
