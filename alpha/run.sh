#!/bin/bash

if [ $# -eq 0 ] ; then
  echo "Missing Hostname"
  exit 1
fi

if [ -z "$MONGO_URI" ] ; then
  echo "Missing Mongo URI"
  exit 1
fi

hostname="$1"

docker run --rm -v /var/run/docker.sock:/var/run/docker.sock      \
  -e HOSTNAME="$hostname"                                         \
  -e MONGO_URI="$MONGO_URI"                                       \
  -e PYTHONUNBUFFERED=1                                           \
  -d                                                              \
  stats-logger:latest

# # #
# #
#
