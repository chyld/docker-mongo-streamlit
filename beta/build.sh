#!/usr/bin/bash


docker build -t event-dashboard:latest .
docker run --rm -p 8501:8501 event-dashboard:latest

