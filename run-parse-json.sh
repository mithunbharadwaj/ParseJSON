#!/bin/bash
mongod --fork --syslog && python3 ./main.py
echo Docker complete