#!/bin/bash
# A scripts that task in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" -s "$1"
