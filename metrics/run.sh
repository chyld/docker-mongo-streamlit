#!/bin/bash

if [ -z "$MYHOSTNAME" ] ; then
  echo "Missing MYHOSTNAME"
  exit 1
fi

if [ -z "$MYAUTHKEY" ] ; then
  echo "Missing MYAUTHKEY"
  exit 1
fi

docker run --rm -d -e MYHOSTNAME="${MYHOSTNAME}" -e MYAUTHKEY="${MYAUTHKEY}" chyld/machinemetrics:latest

