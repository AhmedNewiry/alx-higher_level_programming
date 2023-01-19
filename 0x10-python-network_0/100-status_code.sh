#!/bin/bash
#sends a request to a url and displays the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
