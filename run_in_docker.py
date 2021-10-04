#!/usr//bin/python3

import argparse
import docker
import json
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


parser = argparse.ArgumentParser()
parser.add_argument("command", help="Convert command to run in docker")
args = parser.parse_args()

client = docker.from_env()
container = client.containers.run(get_container_image(
), f"/app/{args.command}", remove=True, detach=True, volumes=config.get("volumes"))

logs = container.logs(stream=True)

for line in logs:
    print(line.decode("utf-8").strip())
