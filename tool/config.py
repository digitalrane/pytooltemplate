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
"""Config handling routines."""

from confuse import Configuration
from argparse import ArgumentParser


class Config(Configuration):
    """Helper class for holding parsed config, extending confuse's BaseConfiguraion class."""

    def __init__(self):
        """Wrap the initialisation of confuse's Configuration object providing defaults for our application."""
        super().__init__("tool", __name__)

        self.parser = ArgumentParser(description="My very cool tool for doing very cool crimes")
        self.parser.add_argument(
            "-l",
            "--log-level",
            type=str,
            default="info",
            nargs="?",
            help="The default log level, valid options are info, warn, error or debug",
            dest="logging.loglevel",
        )
        self.parser.add_argument(
            "-d",
            "--output-dir",
            type=str,
            default="output",
            nargs="?",
            help="The folder to use when saving gathered data.",
            dest="output.folder",
        )
        self.parser.add_argument(
            "-c",
            "--config",
            default="config.yaml",
            help="File to read config from. Defaults to `config.yaml`",
            dest="config.file",
        )
        self.parser.add_argument(
            "--logfile",
            "-L",
            default=None,
            help="File to log to in addition to stdout",
            dest="logging.file",
        )
        self.parser.add_argument(
            "--format",
            "-F",
            choices=["text", "json"],
            default="text",
            help="Format for output",
        )

        args = self.parser.parse_args()
        self.set_args(args, dots=True)
