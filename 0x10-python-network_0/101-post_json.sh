#!/bin/bash
# send json files with POST request
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
