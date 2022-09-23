#!/bin/bash
# A script that displays body size of a request using curl
curl -s --write-out '%{size_download}' -o /dev/null "$1"
