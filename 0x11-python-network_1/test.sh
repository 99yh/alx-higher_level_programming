#!/usr/bin/env sh
# copy a file to the sandbox and run the command after it
host_name='3c2459c87a6d@3c2459c87a6d.8358262e.alx-cod.online'
scp -o 'PasswordAuthentication yes' "$1" "$host_name":/tmp/
ssh -o 'PasswordAuthentication yes' "$host_name" ". /tmp/$1 $2"
