""" https://ozzmaker.com/using-python-with-a-gps-receiver-on-a-raspberry-pi/ """
from gps import *
import time
import json

    
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
try:
    while True:
        my_dict = dict() 
        report = next(gpsd) #
        if report['class'] == 'TPV':
            my_dict['lat'] = getattr(report,'lat',0.0)
            my_dict['lon'] = getattr(report,'lon',0.0)
            my_dict['time'] = getattr(report,'time','')
            json_my_dict = json.dumps(my_dict)
            print(my_dict)  
        time.sleep(1) 
 
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print("Done.\nExiting.")
