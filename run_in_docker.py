#!/usr/bin/env python3

import argparse
import json
import subprocess
from os import path

file_dir = path.dirname(path.abspath(__file__))
config_path = path.join(file_dir, "docker-config.json")

with open(config_path, "r") as read_file:
    config = json.load(read_file)


if not config.get("volumes"):
    print("Config is missing volumes")
    exit


def get_container_image():
    if config.get("image"):
        return config.get("image")

    return "kristofferlarsson/raw-converter"


def get_docker_cmd(volumes, cmd):
    docker_cmd = ["docker", "run"]

    for volume in volumes:
        docker_cmd += ["-v", volume]

    docker_cmd += [get_container_image()]
    docker_cmd += [f"/app/{cmd}"]

    return " ".join(docker_cmd)

parser = argparse.ArgumentParser()
parser.add_argument("command", help="Convert command to run in docker")
args = parser.parse_args()

cmd = get_docker_cmd(config.get("volumes"), args.command)

proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
print(str(proc.stdout.decode("utf-8").strip()))
