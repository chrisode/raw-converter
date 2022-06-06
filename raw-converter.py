#!/usr/bin/env python3

import json
import subprocess
import sys
import time
from os import path


container_name = "raw-converter"
current_time = int(time.time())


def get_config_path():
    file_dir = path.dirname(path.abspath(__file__))
    return path.join(file_dir, "docker-config.json")


def get_docker_config():
    config_path = get_config_path()

    with open(config_path, "r") as read_file:
        config = json.load(read_file)

    return config


def write_docker_config(config):
    config_path = get_config_path()

    with open(config_path, "w+") as file:
        json.dump(config, file, indent=4)


def set_lastpull(config):
    config["lastpull"] = current_time
    write_docker_config(config)


def get_container_image(config):
    if config.get("image"):
        return config.get("image")

    return "kristofferlarsson/raw-converter"


def check_if_image_should_be_pulled(config):
    config = get_docker_config()

    if config.get("pull") == "always":
        return True

    lastpull = config.get("lastpull") or 0
    max_age = current_time - 86400  # 1 day

    if lastpull < max_age:
        return True

    return False


def pull_image(config):
    if not check_if_image_should_be_pulled(config):
        return False

    print("Image either exceeded max age or is forced to be updated - Pulling image")
    cmd = f"docker pull {get_container_image(config)}"
    run_and_pipe_to_dev_null(cmd)

    set_lastpull(config)


def get_docker_run_cmd(config):
    args = " ".join(sys.argv[1:])
    docker_cmd = ["docker", "run", "--name",
                  container_name]

    for volume in config.get("volumes"):
        docker_cmd += ["-v", volume]

    docker_cmd += [get_container_image(config)]
    docker_cmd += [f"/app/convert.py {args}"]

    return " ".join(docker_cmd)


def run_container(config):
    proc = subprocess.run(
        get_docker_run_cmd(config),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print_output(proc.stderr)
    print_output(proc.stdout)


def remove_container():
    run_and_pipe_to_dev_null(f"docker rm {container_name}")


def print_output(output):
    decoded = output.decode("utf-8").strip()
    if decoded:
        print(decoded)


def run_and_pipe_to_dev_null(cmd):
    subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def __main__():
    config = get_docker_config()

    pull_image(config)

    run_container(config)
   
    remove_container()


if __name__ == "__main__":
    __main__()
