#!/bin/bash
#sends a GET request to a servers and displays the response body
curl -fsL "$1" -X GET
