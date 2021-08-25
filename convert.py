#!/usr/bin/python3

import exiftool
import os
import argparse

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()

parser.add_argument("filename", help="File to convert")
parser.add_argument("-f", "--force", action="store_true",
                    help="Force overwriting existing files")

args = parser.parse_args()

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
        print(f"Processing with profile: {profile}")
        return f"-p {profiles_dir}/{profile}"
    except:
        print(f"No profile found for Camera Model: {cameramodel}")
        return ""


def get_output_file(file_to_convert):
    path, ext = os.path.splitext(file_to_convert)
    path = path.replace("convert", "done")
    return f"{path}.jpg"


def convert(file_to_convert, force=False):
    output = get_output_file(file_to_convert)
    output_dir = os.path.dirname(output)

    if force == False and os.path.exists(output):
        print("File already converted", file_to_convert, "\n")
        return

    if os.path.exists(output_dir) == False:
        os.makedirs(os.path.dirname(output))

    print("Converting file:", file_to_convert)
    cmd = f"rawtherapee-cli -o \"{output}\" {get_profile(file_to_convert)} --js3 -q -Y -f -c \"{file_to_convert}\""
    print("Running command:", cmd)
    os.system(cmd)

    print("")


convert(args.filename, args.force)
