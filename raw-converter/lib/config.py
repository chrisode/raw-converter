from os import path
from json import dump as json_dump, load as json_load

filetypes = ("cr2", "rw2", "nef")

def get_container_config_path():
    file_dir = path.dirname(path.abspath(__file__))
    return path.join(file_dir, "..", "config", "container-config.json")


def get_container_config():
    config_path = get_container_config_path()

    with open(config_path, "r") as read_file:
        config = json_load(read_file)

    return config


def write_container_config(config):
    config_path = get_container_config_path()

    with open(config_path, "w+") as file:
        json_dump(config, file, indent=4)