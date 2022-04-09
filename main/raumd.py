import argparse
import sys
import platform
import socket

from .__init__ import __version__

from .runner import run
from .runner import dryrun
from .importer import download
from .configurer import configure
from .configurer import configuration
from .inventory import show

from .console import console
from .graceful_exiter import graceful_exiter

def main():
	description = """Raumdeuter runs your sequence of bash commands defined in a json file."""

	parser = argparse.ArgumentParser(description = description)

	subparsers = parser.add_subparsers()

	run_parser = subparsers.add_parser('run', help = 'Runs a command or a sequence')
	run_parser.add_argument("id", type = str, nargs = '+', help = "The sequence or command to be executed.")
	run_parser.add_argument("--params", type = str, nargs = '*', help = "The parameters to run the sequences with.")
	run_parser.add_argument("--failearly", "-failearly", "-fe", "--fe", action='store_true', help = "If present stops on first command failure.")
	run_parser.add_argument('--verbose', '-verbose', '-v', action='store_true', help = "Print the output of commands.")
	run_parser.set_defaults(func=run)

	download_parser = subparsers.add_parser('download', help = 'Downloads a sequence from airlocks.xyz')
	download_parser.add_argument("id", type = str, nargs = '+', help = "The sequence to obtain.")
	download_parser.add_argument("--rename", type = str, nargs = '*', help = "Renames the sequence for local use.")
	download_parser.set_defaults(func=download)

	dryrun_parser = subparsers.add_parser('dryrun', help = 'Dryruns a command or a sequence')
	dryrun_parser.add_argument("id", type = str, nargs = '+', help = "The sequence or command to be executed.")
	dryrun_parser.add_argument("--params", type = str, nargs = '*', help = "The parameters to run the sequences with.")
	dryrun_parser.set_defaults(func=dryrun)
	
	show_parser = subparsers.add_parser('show', help = 'Shows the existing commands and/or a sequence')
	show_parser.add_argument("id", type = str, nargs = '*', help = "The sequence or command to be executed.")
	show_parser.set_defaults(func=show)

	configure_parser = subparsers.add_parser('configure', help = 'Configures the runner.')
	configure_parser.add_argument("--url", "-u", "-url", "--download-url", "-download-url", type = str, nargs = 1, help = "Sets the download url.")
	configure_parser.add_argument("--path", "-p", "-path", "--download-path", "-download-path", type = str, nargs = 1, help = "Path to json file holding the sequences.")
	configure_parser.add_argument("--localssl", "-localssl", type = str, nargs = 1, help = "Accept locally generated certificates. (Yes/No)")
	configure_parser.add_argument("--timeout", "-t", type = str, nargs = 1, help = "Timeout for every command in seconds.")
	configure_parser.add_argument("--failearly", "-fe", type = str, nargs = 1, help = "General exit strategy. (Yes/No)")
	configure_parser.add_argument("--reset", "-r", action='store_true', help = "Reset configuration to defaults.")
	configure_parser.add_argument("--show", "-show", action='store_true', help = "Show current configuration.")
	configure_parser.add_argument('--verbose', '-verbose', type = str, nargs = 1, help = "Print the output of commands. (Yes/No)")
	configure_parser.set_defaults(func=configure)

	parser.add_argument("-v", "--v", "-version", "--version", action = 'version', version=__version__,
                        default = None, help = "console prints the version of the script.")

	if len(sys.argv) <= 1:
		sys.argv.append('--help')

	args = parser.parse_known_args()

	args[0].func(args[0])

flag = graceful_exiter()

if __name__ == "__main__":
    main() 