#!/bin/bash

while read -r line; do
    if [[ $line =~ ^\>.* ]]; then  # Detect if line starts with '>'
        if [[ $line =~ \[\!TIP\] ]]; then
            echo "!!! tip"        
        elif [[ $line =~ \[\!NOTE\] ]]; then
            echo "!!! note" 
        elif [[ $line =~ \[\!WARNING\] ]]; then
            echo "!!! warning"  
        elif [[ $line =~ \[\!IMPORTANT\] ]]; then
            echo "!!! danger"
        else
            echo "   ${line:1}"
        fi
    else
        # Pass through any line not part of a block
        echo "${line}" | sed -e 's/docs\/assets\/\([a-zA-Z0-9_\-]\+\.\(png\|jpg\|gif\)\)/assets\/\1/g'
    fi

done < README.md > docs/index.md
