#!/bin/bash
# script that sends a GET request to the url and displays the body
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
