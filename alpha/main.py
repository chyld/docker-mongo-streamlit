import os
import time
import docker
from pymongo import MongoClient
from datetime import datetime

mongo_uri = os.environ['MONGO_URI']
hostname = os.environ['HOSTNAME']

dclient = docker.DockerClient()
mclient = MongoClient(mongo_uri)
events = mclient.dashboards.container_events

try:
    while True:
        for c in dclient.containers.list(all=True):
            receive_time = datetime.now()
            attrs = c.attrs
            data = attrs | {'hostname': hostname, 'receive_time': receive_time}
            events.insert_one(data)
            print(f'Data inserted @ {receive_time}')
        time.sleep(10)    
except:
    print('An error occurred')

