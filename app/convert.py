#!/usr/bin/env python3

from os import path
import argparse
import logging

from lib.convert_file import convert_file
from lib.convert_folder import convert_folder

def convert(filepath, output_folder=None, force=False, verbose=False):
    if verbose:
        logging.basicConfig(level=logging.INFO)

    if not path.exists(filepath):
        print("Given file or folder does not exists")
        exit(1)

    if path.isdir(filepath):
        convert_folder(filepath, output_folder=output_folder, force=force)
    else:
        convert_file(filepath, output_folder=output_folder, force=force)


def __main__():
    parser = argparse.ArgumentParser()

    parser.add_argument("filepath", help="File or folder to convert")
    parser.add_argument(
        "-o", "--output", help="Output folder, if not set will it output to same folder as files is in")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose logging")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Force overwriting existing files")

    args = parser.parse_args()

    convert(args.filepath, output_folder=args.output,
            force=args.force, verbose=args.verbose)


if __name__ == "__main__":
    __main__()
