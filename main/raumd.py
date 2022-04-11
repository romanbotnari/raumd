"""script entrypoint. defines arguments, assigns operations to modules."""

import argparse
import sys

from .__init__ import __version__
from .runner import run
from .runner import dryrun
from .importer import download
from .configurer import configure
from .inventory import show
from .graceful_exiter import GracefulExiter

RUN_HELP = 'Runs a command or a sequence.'
RUN_ID_HELP = 'The sequence or command to be executed.'
RUN_PARAMS = 'The parameters to run the sequences with.'
RUN_FAIL_EARLY = 'If present stops on first command failure.'
RUN_VERBOSE = 'Print the output of commands.'

DOWNLOAD_HELP = 'Downloads a sequence from airlocks.xyz'
DOWNLOAD_ID_HELP = 'The sequence to obtain.'
DOWNLOAD_RENAME_HELP = 'Renames the sequence for local use.'

DRY_RUN_HELP = 'Dryruns a command or a sequence.'

SHOW_HELP = 'Shows the existing commands and/or a sequence.'
SHOW_ID_HELP = 'The sequence or command to be executed.'

CONFIG_HELP = 'Configures the runner.'
CONFIG_URL_HELP = 'Sets the download url.'
CONFIG_PATH_HELP = 'Path to json file holding the sequences.'
CONFIG_LOCALSSL_HELP = 'Accept locally generated certificates. (Yes/No)'
CONFIG_TIMEOUT_HELP = 'Timeout for every command in seconds.'
CONFIG_FAILEARLY_HELP = 'General exit strategy. (Yes/No)'
CONFIG_RESET_HELP = 'Reset configuration to defaults.'
CONFIG_SHOW_HELP = 'Show current configuration.'
CONFIG_VERBOSE_HELP = 'Print the output of commands. (Yes/No)'

def main():
    """main function"""
    description = """Raumdeuter runs your sequence of bash commands defined in a json file."""
    parser = argparse.ArgumentParser(description = description)
    subparsers = parser.add_subparsers()

    run_parser = subparsers.add_parser('run',
        help = RUN_HELP)
    run_parser.add_argument("id", type = str, nargs = '+',
        help = RUN_ID_HELP)
    run_parser.add_argument("--params", type = str, nargs = '*',
        help = RUN_PARAMS)
    run_parser.add_argument("--failearly", "-failearly", "-fe", "--fe", action='store_true',
        help = RUN_FAIL_EARLY)
    run_parser.add_argument('--verbose', '-verbose', '-v', action='store_true',
        help = RUN_VERBOSE)
    run_parser.set_defaults(func=run)

    download_parser = subparsers.add_parser('download',
        help = DOWNLOAD_HELP)
    download_parser.add_argument("id", type = str, nargs = '+',
        help = DOWNLOAD_ID_HELP)
    download_parser.add_argument("--rename", type = str, nargs = '*',
        help = DOWNLOAD_RENAME_HELP)
    download_parser.set_defaults(func=download)

    dryrun_parser = subparsers.add_parser('dryrun',
        help = DRY_RUN_HELP)
    dryrun_parser.add_argument("id", type = str, nargs = '+',
        help = RUN_ID_HELP)
    dryrun_parser.add_argument("--params", type = str, nargs = '*',
        help = RUN_PARAMS)
    dryrun_parser.set_defaults(func=dryrun)

    show_parser = subparsers.add_parser('show',
        help = SHOW_HELP)
    show_parser.add_argument("id", type = str, nargs = '*',
        help = SHOW_ID_HELP)
    show_parser.set_defaults(func=show)

    configure_parser = subparsers.add_parser('configure',
        help = CONFIG_HELP)
    configure_parser.add_argument("--url", "-u", "-url", "--download-url", "-download-url",
        type = str, nargs = 1,
        help = CONFIG_URL_HELP)
    configure_parser.add_argument("--path", "-p", "-path", "--download-path", "-download-path",
        type = str, nargs = 1,
        help = CONFIG_PATH_HELP)
    configure_parser.add_argument("--localssl", "-localssl",
        type = str, nargs = 1,
        help = CONFIG_LOCALSSL_HELP)
    configure_parser.add_argument("--timeout", "-t",
        type = str, nargs = 1,
        help = CONFIG_TIMEOUT_HELP)
    configure_parser.add_argument("--failearly", "-fe",
        type = str, nargs = 1,
        help = CONFIG_FAILEARLY_HELP)
    configure_parser.add_argument("--reset", "-r",
        action='store_true',
        help = CONFIG_RESET_HELP)
    configure_parser.add_argument("--show", "-show",
        action='store_true',
        help = CONFIG_SHOW_HELP)
    configure_parser.add_argument('--verbose', '-verbose',
        type = str, nargs = 1,
        help = CONFIG_VERBOSE_HELP)
    configure_parser.set_defaults(func=configure)

    parser.add_argument("-v", "--v", "-version", "--version", action = 'version',
        version=__version__, default = None, help = "console prints the version of the script.")

    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    args = parser.parse_known_args()

    args[0].func(args[0])

flag = GracefulExiter()

if __name__ == "__main__":
    main()
