#!/bin/bash
# Display the response body only if status code is 200
tmp_file="/tmp/response_"$(date +"%N")".txt";http_response=$(curl -s -o "$tmp_file" --write-out "%{http_code}" "$1"); if [ "$http_response" == "200" ]; then cat "$tmp_file"; rm "$tmp_file"; fi
