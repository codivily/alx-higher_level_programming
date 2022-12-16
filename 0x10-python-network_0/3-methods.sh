#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -I -L -s -X OPTIONS "$1" | grep -E "Allow:" | cut -d ":" -f 2 | sed 's/^ *//g'
