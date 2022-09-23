#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of th response
curl -X DELETE -s "$1"
