#!/bin/bash

if [ -z "$MYHOSTNAME" ] ; then
  echo "Missing MYHOSTNAME"
  exit 1
fi

if [ -z "$MYAUTHKEY" ] ; then
  echo "Missing MYAUTHKEY"
  exit 1
fi

docker run -d --rm \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  -e MYHOSTNAME="${MYHOSTNAME}" -e MYAUTHKEY="${MYAUTHKEY}" \
  chyld/machinemetrics:latest \
  --path.rootfs=/host

