# Raw convert

A simple application to batch convert raw files to jpeg. It uses Rawtherapee to convert the rawfiles and applies a custom profile based on what camera used to shoot the picture. You need to create the custom camera profile and put it in the profiles directory, if no profile is found for the camera it will use the default Rawtherapee raw profile.

Given it uses Rawtherapee-cli it is limited to run one instance of this script and cannot be run in parallel, unless you run multiple containers.

## How to use the script
This script can convert a raw file into a jpg or a folder with raw files, including all its subfolders, into jpgs. By default will it use docker to run the script within a container. You can either run it directly `raw-converter/convert.py` or by invoking it with python `python3 raw-converter`.

### Usage
```
usage: convert.py [-h] [-o OUTPUT] [-v] [-f] [--no-container] filepath

positional arguments:
  filepath              File or folder to convert

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output folder, if not set will it output to same folder as files is in
  -v, --verbose         Verbose logging
  -f, --force           Force overwriting existing files
  --no-container        Don't run the script in a container
```
## Setting it up
Before you can use the script do you need to create a config for how it should run the container.

The config file is located in the folder `raw-converter/config`. To set it up copy the example config `/container-config.example.json` to `container-config.json` and add to the volumes array the path to the folder from where you want to convert your photos. The format in the config is in regular docker format for volumes `local_path:container_path`.
