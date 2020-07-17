import json
import subprocess
import os
import time

my_dict = dict()
my_dict['lat'] = 28.50959305
my_dict['lon'] = 77.41020441
my_dict['time'] = "2020-07-16T02:23:41.800Z"

for i in range(100):
    my_dict['lat'] += 0.3
    my_dict['lon'] += 0.2 
    json_my_dict = json.dumps(my_dict)
    with open('/tmp/gps.logs.txt', 'w') as file: 
        file.write(json_my_dict)
    my_process = subprocess.Popen(["scp","/tmp/gps.logs.txt","root@192.168.1.33:/tmp/gps.logs.txt_1"])
    sts = os.waitpid(my_process.pid, 0)
    time.sleep(1)
