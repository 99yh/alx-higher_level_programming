#!/bin/bash
# GET the body of a response if only the status code is 200
curl -sLX PUT -H 'Origin: School' -d 'user_id=98' 0.0.0.0:5000/catch_me_2
