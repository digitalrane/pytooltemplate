#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021
#
# Distributed under terms of the GPL license.

"""Test fixtures for the tool."""

import mock
import os
import pytest
import sys

# bring in top level library to path
test_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, test_path + "/../")


@pytest.fixture
def mocked_pkg_resources(monkeypatch):
    """Mock the pkg_resources library."""
    import pkg_resources

    monkeypatch.setattr(pkg_resources, "require", mock.Mock())


@pytest.fixture
def utils():
    """Provide a test instance of the CLI class."""
    from tool import util

    return util
