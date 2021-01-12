# Raw convert

A simple application to batch convert raw files to jpeg, from one directory to another.

## Scripts

- `batch_convert.sh` - Iterates through the raw images in the folder to convert
- `convert.py` - Converts a raw image from one folder to another, *see help for available parameters*

## How to use docker image

### Volumes the container expects
- `/convert` ***(required)*** - The folder containing all your raw files you want to convert 
- `/done` ***(required)*** - The folder you want to store the generated jpegs in
- `/app/profiles` ***(optional)*** - Rawtherapee profiles that you want to apply to your images 

When running the container it will directly run the batch_convert.sh which will start to iterate through all raw images in the selected folder. 
