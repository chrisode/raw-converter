# Raw convert

A simple application to batch convert raw files to jpeg. It uses Rawtherapee to convert the rawfiles and applies a custom profile based on what camera used to shoot the picture. You need to create the custom camera profile and put it in the profiles directory, if no profile is found for the camera it will use the default Rawtherapee raw profile.

Given it uses Rawtherapee-cli it is limited to run one instance of this script, it cannot be run in parallel.

## Scripts

### convert.py
Converts a raw file to a jpeg
```
$ /app/convert.py -h
usage: convert.py [-h] [-v] [-f] filename

positional arguments:
  filename       File to convert

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Verbose logging
  -f, --force    Force overwriting existing files
```

### batch_convert.py

Iterates through the raw images in a chosen folder to convert

```
$ /app/batch_convert.py -h
usage: batch_convert.py [-h] -c CONVERT [-o OUTPUT] [-f] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -c CONVERT, --convert CONVERT
                        Folder to convert
  -o OUTPUT, --output OUTPUT
                        Output folder, if not set will it output to same folder as files is in
  -f, --force           Force overwriting existing files
  -v, --verbose         Verbose logging
  ```


## How to run in a docker container

You can use a the `run_in_docker.py` script to run a command inside a docker container. This script will create a new container, run the script and then remove the container again. This script replaces the previous use of docker-compose and comes with the perc of allowing us to circumvent the limitation of only being able to run one instance of rawtherapee.

### Setting it up
Before you can use the `run_in_docker.py` script do you need to create a config for it.

**Docker config**

Copy the example config `dokcer-config.example.json` to `docker-config.json` and add the path to the folder from where you want to convert your photos. The format in the config is in regular docker format for volumes `local_path:container_path`.

### Run the script

You need to tell the command which script you want to run and the parameters that script expect. 

Run it like this for example to batch convert all raw files in /convert

`./run_in_docker-py "batch_convert.py -c /convert"`



