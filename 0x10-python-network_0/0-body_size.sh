#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -Is "$1" | grep -i '^Content-Length:' | awk '{print $2}'