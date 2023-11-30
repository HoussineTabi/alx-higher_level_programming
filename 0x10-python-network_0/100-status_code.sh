#!/bin/bash
# Script that sends a request to a url that passed as an argument
curl -s -o >1 -w '%(http_code)' "$1"
