#!/bin/bash
# Script that sends a request to a url that passed as an argument
curl -s -o /dev/null -w '%(http_code)' "$1"
