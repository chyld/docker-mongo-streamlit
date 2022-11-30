import os
import docker
from pymongo import MongoClient
from datetime import datetime

mongo_uri = os.environ['MONGO_URI']
hostname = os.environ['HOSTNAME']

dclient = docker.DockerClient()
mclient = MongoClient(mongo_uri)
events = mclient.dashboards.container_events

for event in dclient.events(decode=True):
    receive_time = datetime.now()
    megaevent = event | {'hostname': hostname, 'receive_time': receive_time}
    print(f'Received event @ {receive_time}')
    events.insert_one(megaevent)

