#!/usr/bin/env python3
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
"""Main entrypoint for the CLI."""
from tool.config import Config
from tool.logging import Logger
import logging
import os.path
import pkg_resources
import yaml
import sys


class Cli:
    """Core class of the CLI."""

    some_class_var = {}

    def __init__(self):
        """Create new CLI and configure runtime environment."""
        self.config = Config()
        self.logger = Logger(self.config["logging"]["loglevel"].get())
        self.output_format = self.config["format"].get()

        # disable logging for non-text output formats
        if self.output_format != "text":
            logging.disable(level=logging.CRITICAL)

        # get the version of the current package if available
        # this will fail if not running from an installed package
        # e.g. during unit tests
        try:
            self.version = pkg_resources.require("tool")[0].version
        except pkg_resources.DistributionNotFound:
            self.version = "unknown"

    def startup_message(self):
        """Print startup message to log."""
        self.logger.info(
            (
                "l33t t00l version {} starting...\n"
                "\t* Config directory: {}\n"
                "\t* Log level: {}\n"
            ).format(
                self.version,
                self.config.config_dir(),
                self.config["logging"]["loglevel"].get(),
            )
        )

    def usage(self):
        """Print program usage."""
        self.config.parser.print_help()

    def run(self):
        """Run the main process."""
        self.logger.error("this tool doesn't do anything yet")

def main():
    """Program entry point."""
    cli = Cli()
    cli.startup_message()
    # this can be removed and replaced with just cli.run() if no mandatory args
    if "some-important-flag" in cli.config:
        cli.run()
    else:
        cli.usage()
