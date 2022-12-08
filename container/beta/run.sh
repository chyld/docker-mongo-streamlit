#!/bin/bash

if [ -z "$MONGO_URI" ] ; then
  echo "Missing Mongo URI"
  exit 1
fi

docker run --rm                                                   \
  -e MONGO_URI="$MONGO_URI"                                       \
  -p 8501:8501                                                    \
  -d                                                              \
  stats-dashboard:latest

# # #
# #
#
