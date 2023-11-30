#!/bin/bash
# Script takes in a url and sends a GET request to the url
curl -s "$1" -X GET -H "X-School-User-Id: 98"
