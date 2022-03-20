#!/usr/bin/python3

import os
import argparse

from convert import convert

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--convert", required=True, help="Folder to convert")
parser.add_argument(
    "-o", "--output", help="Output folder, if not set will it output to same folder as files is in")
parser.add_argument("-f", "--force", action="store_true",
                    help="Force overwriting existing files")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Verbose logging")

args = parser.parse_args()

if not os.path.exists(args.convert):
    print("Folder to convert does not exists")


def get_files_to_convert(folder):
    items = os.listdir(folder)

    files_to_convert = []
    filetypes = (".cr2", "rw2")

    for item in items:
        fullpath = os.path.join(folder, item)
        if (item.lower().endswith(filetypes)):
            files_to_convert.append(fullpath)
            next

        if os.path.isdir(fullpath):
            files_to_convert = files_to_convert + \
                get_files_to_convert(fullpath)

    return files_to_convert


files_to_convert = get_files_to_convert(args.convert)

for file in files_to_convert:
    convert(file, from_folder=args.convert, output_folder=args.output,
            force=args.force, verbose=args.verbose)
