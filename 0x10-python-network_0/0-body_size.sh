#!/usr/bin/env bash
# bash script that takes in a URL and sends a request to that URL
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")
echo "$response"
