FROM ubuntu:latest

COPY ./node_exporter /bin/node_exporter
COPY ./start.sh /bin/start.sh

RUN apt update && apt install -y curl
RUN curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.noarmor.gpg | tee /usr/share/keyrings/tailscale-archive-keyring.gpg >/dev/null
RUN curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.tailscale-keyring.list | tee /etc/apt/sources.list.d/tailscale.list
RUN apt update && apt install -y tailscale

EXPOSE      9100
ENTRYPOINT  [ "start.sh" ]

