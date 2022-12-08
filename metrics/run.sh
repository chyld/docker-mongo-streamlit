#!/bin/bash

if [ -z "$MYHOSTNAME" ] ; then
  echo "Missing MYHOSTNAME"
  exit 1
fi

if [ -z "$MYAUTHKEY" ] ; then
  echo "Missing MYAUTHKEY"
  exit 1
fi

docker run \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  -e MYHOSTNAME="${MYHOSTNAME}" -e MYAUTHKEY="${MYAUTHKEY}" \
  --path.rootfs=/host \
  chyld/machinemetrics:latest

