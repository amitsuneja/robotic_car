#! /usr/bin/python
 
from gps import *
import time
    
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
print('latitude\tlongitude\ttime utc\t\t\taltitude\tepv\tept\tspeed\tclimb') # '\t' = TAB to try and output the data in columns.
   
try:
 
 
    while True:
        report = next(gpsd) #
        if report['class'] == 'TPV':
#            print(report['lat'],"\t", end=' ')
#            print(report['lon'],"\t", end=' ')
#            print(report['time'],"\t", end=' ')
#            print(report['alt'],"\t", end=' ')
#            print(report['epv'],"\t", end=' ')
#            print(report['ept'],"\t", end=' ')
#            print(report['speed'],"\t", end=' ')
#            print(report['climb'],"\t", end=' ')
#            print("\n")
             
            print(getattr(report,'lat',0.0),"\t", end=' ')
            print(getattr(report,'lon',0.0),"\t", end=' ')
            print(getattr(report,'time',''),"\t", end=' ')
            print(getattr(report,'alt','nan'),"\t", end=' ')
            print(getattr(report,'epv','nan'),"\t", end=' ')
            print(getattr(report,'ept','nan'),"\t", end=' ')
            print(getattr(report,'speed','nan'),"\t", end=' ')
            print(getattr(report,'climb','nan'),"\t")
 
        time.sleep(1) 
 
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print("Done.\nExiting.")
