#!/bin/bash
#sends a Delete request to a server and displays the response body
curl -s "$1" -X DELETE
