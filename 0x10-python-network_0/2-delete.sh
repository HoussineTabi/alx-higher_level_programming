#!/bin/bash
# sends a delete request to the url at the first argument
curl -s "$1" -X DELETE
