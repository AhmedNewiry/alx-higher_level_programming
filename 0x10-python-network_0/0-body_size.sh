#!/bin/bash
#takes in a url, sends a request to that url and display the response body size
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
