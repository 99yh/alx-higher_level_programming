#!/bin/bash
# GET the body of a response if only the status code is 200
curl -sI "$1" | grep -q '200 OK' && curl -s "$1"
