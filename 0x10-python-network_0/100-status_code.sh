#!/bin/bash
# Display only the statu scode of the response
curl -s --write-out '%{http_code}\n' -o /dev/null "$1"
