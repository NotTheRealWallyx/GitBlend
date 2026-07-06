import argparse
import unittest
from unittest.mock import patch

from gitblend.commands.commits.entrypoints import add_commits_commands


def build_parser():
    parser = argparse.ArgumentParser(prog="gitblend")
    subparsers = parser.add_subparsers(dest="command")
    add_commits_commands(subparsers)
    return parser


class TestCommitEntrypoints(unittest.TestCase):

    @patch("gitblend.commands.commits.entrypoints.load_config", return_value={})
    def test_commit_flags_default_to_false_without_config(self, mock_config):
        parser = build_parser()
        args = parser.parse_args(["commit", "-m", "Initial commit"])

        self.assertEqual(args.message, "Initial commit")
        self.assertFalse(args.add)
        self.assertFalse(args.sign)
        self.assertFalse(args.allow_empty)

    @patch(
        "gitblend.commands.commits.entrypoints.load_config",
        return_value={"commit": {"add": True, "sign": True, "allow_empty": True}},
    )
    def test_commit_flags_default_from_config(self, mock_config):
        parser = build_parser()
        args = parser.parse_args(["commit", "Initial commit"])

        self.assertEqual(args.positional_message, "Initial commit")
        self.assertTrue(args.add)
        self.assertTrue(args.sign)
        self.assertTrue(args.allow_empty)

    @patch("gitblend.commands.commits.entrypoints.load_config", return_value={})
    def test_commit_accepts_positional_message(self, mock_config):
        parser = build_parser()
        args = parser.parse_args(["commit", "Initial commit"])

        self.assertEqual(args.positional_message, "Initial commit")
        self.assertIsNone(args.message)


if __name__ == "__main__":
    unittest.main()
