#!/bin/bash
# Display only the statu scode of the response
curl -s --write-out '%{http_code}' -o /dev/null "$1"
