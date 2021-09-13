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



## How to use docker image

By itself this container will do nothing. The job to convert will start once you run the scripts. 

`docker exec -it raw-converter /app/batch_convert.py -c /convert`

### Volumes the container expects
- `/convert` ***(required)*** - The folder containing all your raw files you want to convert
- `/app/profiles` ***(optional)*** - Rawtherapee profiles that you want to apply to your pictures 


