import exiftool
import os
import subprocess
import logging
from .config import filetypes


def convert_file(file, from_folder=None, output_folder=None, force=False):
    if not file.lower().endswith(filetypes):
        print("File is not one of the supported filetypes:", ", ".join(filetypes))
        return False

    output = get_output_filepath(file, from_folder, output_folder)
    output_dir = os.path.dirname(output)

    if force == False and os.path.exists(output):
        print("File already converted:", file, "|", "Exists as:", output)
        return

    if os.path.exists(output_dir) == False:
        os.makedirs(os.path.dirname(output))

    print("Converting file:", file, "|", "Store as:", output)
    cmd = f"rawtherapee-cli -o \"{output}\" {get_profile(file)} --js3 -q -Y -f -c \"{file}\""
    run_cmd(cmd)


def run_cmd(cmd):
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
    logging.info(str(proc))


def get_output_filepath(file, folder=None, output_folder=None):
    path, ext = os.path.splitext(file)

    if output_folder and folder:
        path = path.replace(folder, output_folder)

    return f"{path}.jpg"


def get_profiles_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.dirname(dir_path)
    return f"{parent_path}/profiles"


def get_available_profiles():
    if not os.path.exists(get_profiles_dir()):
        return []

    profiles = [x for x in os.listdir(
        get_profiles_dir()) if x.endswith(".pp3")]
        
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
        return f"-p {get_profiles_dir()}/{profile}"
    except:
        logging.info(f"No profile found for Camera Model: {cameramodel}")
        return "-d"
