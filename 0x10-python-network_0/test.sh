#!/usr/bin/env sh
# copy a file to the sandbox and run the command after it
scp -o 'PasswordAuthentication yes' "$1" d5ea71da33c8@d5ea71da33c8.f48b819b.alx-cod.online:/tmp/
ssh -o 'PasswordAuthentication yes' d5ea71da33c8@d5ea71da33c8.f48b819b.alx-cod.online ". /tmp/$1 $2"
