#!/bin/bash

# Kill any gunicorn processes running on port 5007
lsof -i :5007 | awk 'NR!=1 {print $2}' | xargs kill -9

# Start gunicorn on port 5007
gunicorn app:app -b :5007
