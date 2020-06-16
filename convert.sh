#!/bin/bash

FOLDER_TO_CONVERT="/convert"
DONE_FOLDER="/done"
THREADS=4

if [ ! -z $1 ] ; then
    FOLDER_TO_CONVERT=$1
fi

if [ ! -z $2 ] ; then
    DONE_FOLDER=$2
fi

function convert() {
    FILE=$1
    OUTPUT=${FILE/$FOLDER_TO_CONVERT/$DONE_FOLDER}
    OUTPUT=${OUTPUT/.CR2/.jpg}
    OUTPUT=${OUTPUT/.RW2/.jpg}
    FILE_DIR=`dirname "$OUTPUT"`
  
    mkdir -p "$FILE_DIR"
    
    ufraw-batch "$FILE" --wb=camera --lensfun=auto --overwrite --out-type=jpeg --output "$OUTPUT";
}
export -f convert
export FOLDER_TO_CONVERT
export DONE_FOLDER

find $FOLDER_TO_CONVERT -type f -name '*.CR2' -print0 -o -name '*.RW2' -print0 | xargs -0 -n 1 -P $THREADS -I {} bash -c 'convert "$@"' _ {} 

unset convert
unset FOLDER_TO_CONVERT
unset DONE_FOLDER

 exit 0