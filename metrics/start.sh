#!/bin/bash

tailscaled --tun=userspace-networking 1> /dev/null  2> /dev/null &
tailscale up --hostname="${MYHOSTNAME}" --authkey="${MYAUTHKEY}"
node_exporter

