#!/bin/bash

function changeExtension() {
    local EXTENSIONS=".CR2 .RW2 .NEF .DNG .cr2 .rw2 .nef .dng"
    local FILE=$1

    for EXT in $EXTENSIONS
    do
        FILE=${FILE/$EXT/.jpg}

        if [[ $FILE == *".jpg" ]]; then
            break
        fi
    done 

    echo $FILE
    return 0  
}

export -f changeExtension