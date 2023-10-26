#!/bin/bash

# curl 'http://192.168.1.30:5001/rewordme' \
#   -H "Content-Type: application/json" \
#   -d '{
#   "disposition" : "You are a Computer Science Ph.D. candidate, who is trying to be informal.",
#     "setup" : "You will be given text that could possibly garbled and filled with grammer errors. You need to reword it so that it makes sense.",
#     "requestString" : f"please reword this text: {rewordString}"
#   }'

URL='http://192.168.1.30:5001/rewordme'
disposition='You are a Computer Science Ph.D. candidate, who is trying to be informal.'
setup='You will be given text that could possibly garbled and filled with grammer errors. You need to reword it so that it makes sense.'
requestString='Hi carolyn, I want to talk to you about getting into final five of survivor.'
username='jfolk'

curl -X POST ${URL} \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "username=${username}&disposition=${disposition}&setup=${setup}&requestString=${requestString}"
