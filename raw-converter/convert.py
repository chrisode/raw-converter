#!/usr/bin/env python3

import sys
import argparse
import logging

from lib.container import run_in_container
from lib.convert import convert

def setup_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("filepath", help="File or folder to convert")
    parser.add_argument("-o", "--output",
                        help="Output folder, if not set will it output to same folder as files is in")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose logging")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Force overwriting existing files")
    parser.add_argument("--no-container", action="store_true",
                        help="Don't run the script in a container")

    return parser


def __main__():
    parser = setup_parser()

    args = parser.parse_args()

    if args.verbose == True:
        logging.basicConfig(level=logging.INFO)

    if args.no_container == True:
        convert(args.filepath, output_folder=args.output, force=args.force)
        return

    run_in_container(sys.argv[1:])


if __name__ == "__main__":
    __main__()
