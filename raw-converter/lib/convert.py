import logging
from os import path

from lib.convert_file import convert_file
from lib.convert_folder import convert_folder


def convert(filepath, output_folder=None, force=False):
    if not path.exists(filepath):
        logging.error("Given file or folder does not exists")
        return False

    if path.isdir(filepath):
        convert_folder(filepath, output_folder=output_folder, force=force)
    else:
        convert_file(filepath, output_folder=output_folder, force=force)
