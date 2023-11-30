#!/bin/bash
#takes in a url, and displays all http methods server will accept
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
