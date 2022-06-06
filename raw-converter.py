#!/usr/bin/env python3

import json
import subprocess
import sys
from os import path


container_name = "raw-converter"


def get_docker_config():
    file_dir = path.dirname(path.abspath(__file__))
    config_path = path.join(file_dir, "docker-config.json")

    with open(config_path, "r") as read_file:
        config = json.load(read_file)

    return config


def get_container_image(config):
    if config.get("image"):
        return config.get("image")

    return "kristofferlarsson/raw-converter"


def get_docker_cmd(args):
    config = get_docker_config()

    docker_cmd = ["docker", "run", "--name",
                  container_name]

    for volume in config.get("volumes"):
        docker_cmd += ["-v", volume]

    docker_cmd += [get_container_image(config)]
    docker_cmd += [f"/app/convert.py {args}"]

    return " ".join(docker_cmd)


def __main__():
    args = " ".join(sys.argv[1:])

    cmd = get_docker_cmd(args)

    proc = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    print(str(proc.stderr.decode("utf-8").strip()))
    print(str(proc.stdout.decode("utf-8").strip()))

    subprocess.run(f"docker rm {container_name}", shell=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == "__main__":
    __main__()
