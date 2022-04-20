# Name: Wade Moulton
# Date: 09/25/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North

from datetime import datetime
import urllib
import requests
import json

# set variables
user_id = 'Boatshoes24'
user_apiid = 'xxxxxxxxxxxxxxxxxxxxxxxx'
zip_code = 30144

# set url for http request
getURL = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={user_apiid}&units=imperial'


def main():
    # retrieve request and decode to json
    response = urllib.request.urlopen(getURL)
    decoded_response = response.read().decode('utf-8')
    json_res = json.loads(decoded_response)

    print(f"Name:\t\t\t\t\t{json_res['name']}")
    print(f"Current Temperature:\t{json_res['main']['temp']} degrees Fahrenheit")
    print(f"Atmospheric Pressure:\t{json_res['main']['pressure']} hPa")
    print(f"Wind Speed:\t\t\t\t{json_res['wind']['speed']} mph")
    print(f"Wind Direction:\t\t\t{json_res['wind']['deg']}")
    timestamp = json_res['dt']
    dt_object = datetime.fromtimestamp(timestamp)
    print(f"Time of Report:\t\t\t{dt_object}")


if __name__ == '__main__':
    main()

