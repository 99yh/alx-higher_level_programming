#!/bin/bash
# GET the body of a response if only the status code is 200
curl -sI -o /dev/null -w "%{http_code}" "$1"
