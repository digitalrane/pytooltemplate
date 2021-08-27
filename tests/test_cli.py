#!/usr/bin/python3
"""Test the CLI."""

from tool.cli import Cli


def test_pytest():
    """Test that pytest itself works."""
    assert True


def test_cli_fixture(cli):
    """Test if the CLI fixture works."""
    assert isinstance(cli, Cli)
