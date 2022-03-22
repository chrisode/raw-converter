#!/usr/bin/env python3

import logging
import os
import argparse

from lib.convert_folder import convert_folder


def batch_convert(convert, output_folder=None, force=False, verbose=False):
    if verbose:
        logging.basicConfig(level=logging.INFO)

    if not os.path.exists(convert):
        print("Folder to convert does not exists")

    convert_folder(convert, output_folder=output_folder, force=force)


def __main__():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--convert", required=True,
                        help="Folder to convert")
    parser.add_argument(
        "-o", "--output", help="Output folder, if not set will it output to same folder as files is in")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Force overwriting existing files")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose logging")

    args = parser.parse_args()

    batch_convert(args.convert, output_folder=args.output,
                  force=args.force, verbose=args.verbose)


if __name__ == "__main__":
    __main__()
