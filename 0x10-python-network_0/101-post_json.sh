#!/bin/bash
# Display only the statu scode of the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d "@$2" 
