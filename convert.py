#!/usr/bin/python3

import exiftool
import os
import argparse
import subprocess
import logging

dir_path = os.path.dirname(os.path.realpath(__file__))
profiles_dir = f"{dir_path}/profiles"


def get_available_profiles():
    if not os.path.exists(profiles_dir):
        return []

    profiles = [x for x in os.listdir(profiles_dir) if x.endswith(".pp3")]

    return profiles


def get_profile(path):
    profiles = get_available_profiles()

    with exiftool.ExifTool() as et:
        cameramodel = et.get_tag("Model", path)

    profile_name = cameramodel.replace(" ", "-").lower() + ".pp3"

    try:
        index = profiles.index(profile_name)
        profile = profiles[index]
        logging.info(f"Processing with profile: {profile}")
        return f"-p {profiles_dir}/{profile}"
    except:
        logging.info(f"No profile found for Camera Model: {cameramodel}")
        return "-d"


def get_output_file(file_to_convert, from_folder=None, output_folder=None):
    path, ext = os.path.splitext(file_to_convert)

    if output_folder and from_folder:
        path = path.replace(from_folder, output_folder)

    return f"{path}.jpg"


def convert(file_to_convert, from_folder=None, output_folder=None, force=False, verbose=False):
    if verbose:
        logging.basicConfig(level=logging.INFO)

    output = get_output_file(file_to_convert, from_folder, output_folder)
    output_dir = os.path.dirname(output)

    if force == False and os.path.exists(output):
        print("File already converted:",
              file_to_convert, "|", "Exists as:", output)
        return

    if os.path.exists(output_dir) == False:
        os.makedirs(os.path.dirname(output))

    print("Converting file:", file_to_convert, "|", "Store as:", output)
    cmd = f"rawtherapee-cli -o \"{output}\" {get_profile(file_to_convert)} --js3 -q -Y -f -c \"{file_to_convert}\""
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    logging.info(str(proc))


def __main__():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="File to convert")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose logging")
    parser.add_argument("-f", "--force", action="store_true",
                        help="Force overwriting existing files")

    args = parser.parse_args()

    convert(args.filename, force=args.force, verbose=args.verbose)


if __name__ == "__main__":
    __main__()
