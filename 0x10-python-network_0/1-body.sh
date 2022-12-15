#!/bin/bash
# Display the response body only if status code is 200
response=$(curl -L -sw "%{http_code}" "$1"); status_code="${response:${#response}-3}"; if [[ "$status_code" -eq 200 ]]; then echo "${response:0:${#response}-3}"; fi
