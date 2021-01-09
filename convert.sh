#!/bin/bash

MYDIR="$(dirname "$(which "$0")")"

source $MYDIR/lib/changeExtension.sh

FOLDER_TO_CONVERT="/convert"
DONE_FOLDER="/done"
FORCE=false

while getopts ":i:o:f" opt; do
  case $opt in
    i) FOLDER_TO_CONVERT="$OPTARG"
    ;;
    o) DONE_FOLDER="$OPTARG"
    ;;
    f) FORCE=true
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    exit 1
    ;;
  esac
done

function convert() {
    FILE=$1
    
    OUTPUT="${FILE/$FOLDER_TO_CONVERT/$DONE_FOLDER}"
    OUTPUT=`changeExtension $OUTPUT`
    OUTPUT_DIR=`dirname "$OUTPUT"`
  
    mkdir -p "$OUTPUT_DIR"

    if [[ -d $OUTPUT ]] ; then
        return
    fi

    if [[ -f $OUTPUT ]]; then
        if [ "$FORCE" = true ] ; then
            echo "Image exists, removing $OUTPUT"
            rm $OUTPUT
        else
            echo "Skipping existing image $FILE - $OUTPUT"
            return
        fi
    fi

    rawtherapee-cli -o $OUTPUT -js3 -q -f -Y -c $FILE    
}

export -f convert
export FOLDER_TO_CONVERT
export DONE_FOLDER
export FORCE

find $FOLDER_TO_CONVERT -type f -name '*.CR2' -print0 -o -name '*.RW2' -print0 | xargs -0 -n 1 -I {} bash -c 'convert "$@"' _ {} 

unset convert
unset changeExtension
unset FOLDER_TO_CONVERT
unset DONE_FOLDER
unset FORCE

exit 0