#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -I -L -s -X OPTIONS "$1" | head -n 2 | tail -n 1 | cut -d ":" -f 2 | sed 's/^ *//g'
