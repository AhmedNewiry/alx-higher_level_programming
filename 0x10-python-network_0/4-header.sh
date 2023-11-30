#!/bin/bash
#takes in a url, sends a GET request and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
