import re
import os
import docker
import subprocess
from pymongo import MongoClient
from datetime import datetime

output = subprocess.run(['ip', 'route'], capture_output=True)
output = output.stdout.decode()
first_line = output.split('\n')[0]
matches = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', first_line)
host_ip = matches[0]
host_name = os.environ['HOST']

dclient = docker.DockerClient(base_url=f'tcp://{host_ip}:2375')
mclient = MongoClient(host_ip, 27017)
events = mclient.eventdb.events

for event in dclient.events(decode=True):
    print(f'Received event @ {datetime.now()}')
    megaevent = event | {'host': host_name, 'ip': host_ip}
    events.insert_one(megaevent)
