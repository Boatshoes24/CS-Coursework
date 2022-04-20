# Name: Wade Moulton
# Date: 11/10/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Mod_6 Assignment

# import requests to send our server request
import requests
# import pprint to make the output of the json in console look nicer
import pprint

# set url to localhost and the correct port
url = 'http://127.0.0.1:12345'

# set variables for the area_id and location_id to make requests
area_id = 5
location_id = 11

# list of all the requests that can be made
urlOptions = [
    f"/area",
    f"/area/{area_id}/location",
    f"/location/{location_id}/measurement",
    f"/area/{area_id}/category",
    f"/area/{area_id}/average_measurement",
    f"/area/{area_id}/number_locations"
]

# send request with options and receive response
req = requests.get(url + urlOptions[5])
# generate error if given a bad server response
req.raise_for_status()

# assign json response from req to response
res = req.json()
# print status code
print("Status: " + str(req.status_code))
# imported pprint just to make the console output look nicer
pprint.pprint(res)
