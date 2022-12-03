import os
import time
import docker
from pymongo import MongoClient
from datetime import datetime

mongo_uri = os.environ["MONGO_URI"]
hostname = os.environ["HOSTNAME"]

dclient = docker.DockerClient()
mclient = MongoClient(mongo_uri)
stats = mclient.dashboards.container_stats

try:
    while True:
        for c in dclient.containers.list(all=True):
            receive_time = datetime.now()
            image = c.attrs["Config"]["Image"]
            is_running = c.attrs["State"]["Running"]
            data = {
                "hostname": hostname,
                "receive_time": receive_time,
                "image": image,
                "is_running": is_running,
            }
            stats.insert_one(data)
            print(f"Data inserted @ {data}")
        time.sleep(300)
except:
    print("An error occurred")
