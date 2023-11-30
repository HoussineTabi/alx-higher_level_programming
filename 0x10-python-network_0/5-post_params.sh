#!/bin/bash
#Script that takes in a url and sends a POST request ot the passed url
curl -s "$1" -X -d "email=test@gmail.com&subject=I will always be here for PLD"
