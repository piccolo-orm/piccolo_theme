#!/bin/bash

./scripts/run-docs.sh & 
while ! nc -z localhost 8000
  do 
    echo "Not Connected"
    sleep 1
done

pytest ./e2e/test_homepage.py 

