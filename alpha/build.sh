#!/usr/bin/bash

# To invoke
# ./build.sh <HOSTNAME>

if [ $# -eq 0 ] ; then
  echo "Missing hostname"
  exit 1
fi

docker build -t event-logger:latest .

docker run --rm --mount type=bind,source=/var/run/docker.sock,destination=/var/run/docker.sock \
  -e HOSTNAME="$1"                                                                             \
  -e MONGO_URI="mongodb://172.17.0.1:27017"                                                    \
  -e PYTHONUNBUFFERED=1                                                                        \
  -d                                                                                           \
  event-logger:latest

