#!/bin/bash
# takes in a url and displays all http methods the server will accept

curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'