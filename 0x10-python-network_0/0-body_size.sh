#!/usr/bin/bash
# A script that displays body size of a request using curl
curl --write-out '%{size_request}\n' -s -o /dev/null "$1"
