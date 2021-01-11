# Raw convert

A simple application to batch convert raw files in a directory to jpeg.

## How to use docker image

The docker image expects three volumes mounted

- `/convert` - The folder containing all your raw files you want to convert
- `/done` - The folder you want to store the generated jpegs in
- `/app/profiles` - Rawtherapee profiles that you want to apply to your images 


