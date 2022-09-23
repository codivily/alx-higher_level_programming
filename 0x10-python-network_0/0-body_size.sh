#!/usr/bin/env bash
# A scripts that tasks in a URL, sends a request to that URL,
# and displays the size of the body of the response
curl --write-out '%{size_request}\n' -s -o /dev/null "$1"
