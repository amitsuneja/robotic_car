import random
import sys
import math
import json

latitude = 28.53
longitude = 77.39
file_n = 'location.log'
my_dict = dict()
my_dict_inner = dict()

def generate_random_data(latitude, longitude, file_name):
    dec_lat = random.random()/100
    dec_lon = random.random()/100
    latitude = latitude + dec_lat
    longitude = longitude + dec_lon
    with open(file_name, 'w') as my_file_handler:
            my_dict_inner["lat"] = latitude
            my_dict_inner["lng"] = longitude
            my_dict["location"] = my_dict_inner
            my_file_handler.write(json.dumps(my_dict))
            my_file_handler.write("\n")
             
            
generate_random_data(latitude, longitude, file_n)
