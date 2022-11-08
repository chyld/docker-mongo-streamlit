# docker build -t event-logger:latest .
# docker run -p 27017:27017 -d mongo
# docker run --rm -e HOST=$(hostname) -e PYTHONUNBUFFERED=1 -d event-logger:latest
# docker logs -f CONTAINER_ID
# docker run --rm -it --mount type=bind,source=/var/run/docker.sock,destination=/var/run/docker.sock event-logger:latest bash 

