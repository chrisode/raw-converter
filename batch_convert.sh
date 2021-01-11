#!/bin/bash

MYDIR="$(dirname "$(which "$0")")"

find /convert -type f -name '*.CR2' -print0 -o -name '*.RW2' -print0 | xargs -0 -n 1 -I {} python3 $MYDIR/convert.py $@ {} 

exit 0