import os
import time
import docker
from pymongo import MongoClient
from datetime import datetime

mongo_uri = os.environ['MONGO_URI']
hostname = os.environ['HOSTNAME']

dclient = docker.DockerClient()
mclient = MongoClient(mongo_uri)
stats = mclient.dashboards.container_stats

try:
    while True:
        for c in dclient.containers.list(all=True):
            receive_time = datetime.now()
            attrs = c.attrs
            data = attrs | {'hostname': hostname, 'receive_time': receive_time}
            stats.insert_one(data)
            print(f'Data inserted @ {receive_time}')
        time.sleep(60)    
except:
    print('An error occurred')
