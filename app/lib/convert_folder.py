from .convert_file import convert_file
from .config import filetypes
import os


def convert_folder(folder, output_folder=None, force=False):
    files_to_convert = get_files_to_convert(folder)

    for file in files_to_convert:
        convert_file(
            file,
            from_folder=folder,
            output_folder=output_folder,
            force=force
        )


def get_files_to_convert(folder):
    items = os.listdir(folder)

    files_to_convert = []

    for item in items:
        fullpath = os.path.join(folder, item)
        if (item.lower().endswith(filetypes)):
            files_to_convert.append(fullpath)
            next

        if os.path.isdir(fullpath):
            files_to_convert += get_files_to_convert(fullpath)

    return files_to_convert
