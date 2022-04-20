# Name: Wade Moulton
# Date: 11/10/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Mod_6 Assignment

# imports
from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

# create server connection
db_connect = create_engine('sqlite:///measures.db')
app = Flask(__name__)
api = Api(app)


# function to generate list of all areas in the db
class Area(Resource):
    def get(self):
        # connect to db and assign query results to query variable
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM area").cursor.fetchall()
        # initialize empty list to store values in for response
        res_list = []
        # iterate query items and create dictionary of key/value pairs and append to response list
        for item in query:
            temp_dict = {
                'area_id': item[0],
                'name': item[1],
                'long': item[2],
                'lat': item[3]
            }
            res_list.append(temp_dict)
        # return json of response list
        return jsonify(res_list)


# function to get all locations for a given area_id
class AreaLocation(Resource):
    def get(self, area_id):
        conn = db_connect.connect()
        # assign values from db that match query
        query = conn.execute(f"SELECT * FROM location WHERE location_area = {int(area_id)}").cursor.fetchall()
        # initialize response list
        res_list = []
        # iterate query results and create dictionary of key/value pairs to append to response list
        for item in query:
            temp_dict = {
                'location_id': item[0],
                'name': item[1],
                'altitude': item[2],
                'area_id': item[3]
            }
            res_list.append(temp_dict)
        # return json of response list
        return jsonify(res_list)


# function to get all measurement values for a given location_id
class LocationMeasurement(Resource):
    def get(self, location_id):
        conn = db_connect.connect()
        # query db and assign results to query variable
        query = conn.execute(f"SELECT * FROM measurement "
                             f"WHERE measurement_location = {int(location_id)}").cursor.fetchall()
        # initialize response list
        res_list = []
        # iterate items in query and assign key/value pairs to dictionary and append to response list
        for item in query:
            temp_dict = {
                'measurement_id': item[0],
                'value': item[1],
                'location_id': item[2]
            }
            res_list.append(temp_dict)
        # return json of response list
        return jsonify(res_list)


# function to return all categories to which a given area belongs
class AreaCategory(Resource):
    def get(self, area_id):
        conn = db_connect.connect()
        # assign query results to variable
        query = conn.execute(f"SELECT category.category_id, category.name, category.description "
                             f"FROM category, category_area "
                             f"WHERE category_area.area_id ={int(area_id)} "
                             f"AND category.category_id=category_area.category_id").cursor.fetchall()
        # initialize response list
        res_list = []
        # iterate items in query and assign key/value pairs to dictionary and append to response list
        for item in query:
            temp_dict = {
                'category_id': item[0],
                'name': item[1],
                'description': item[2]
            }
            res_list.append(temp_dict)
        # return json of response list
        return jsonify(res_list)


# function to give the average measurement for a given area
class AreaAverageMeasurement(Resource):
    def get(self, area_id):
        conn = db_connect.connect()
        # assign query results to query variable
        query = conn.execute(f"SELECT measurement.value "
                             f"FROM measurement, location "
                             f"WHERE location.location_area={int(area_id)} "
                             f"AND measurement.measurement_location=location.location_id").cursor.fetchall()
        # initialize total value
        total = 0
        # iterate through items in query and add each value to total
        for item in query:
            total += item[0]
        # divide total by the amount of items in the query to get the avg
        avg = total/len(query)
        # return the avg
        return avg


# get the number of locations for a given area
class AreaNumberLocations(Resource):
    def get(self, area_id):
        conn = db_connect.connect()
        # submit query to db and assign response
        query = conn.execute(f"SELECT * FROM location "
                             f"WHERE location_area={int(area_id)}").cursor.fetchall()
        # can just return the length of query since we're just looking for a total # of locations
        return len(query)


# add all of our paths to the api
api.add_resource(Area, '/area')
api.add_resource(AreaLocation, '/area/<area_id>/location')
api.add_resource(LocationMeasurement, '/location/<location_id>/measurement')
api.add_resource(AreaCategory, '/area/<area_id>/category')
api.add_resource(AreaAverageMeasurement, '/area/<area_id>/average_measurement')
api.add_resource(AreaNumberLocations, '/area/<area_id>/number_locations')

# initiate server and listen on port 12345
if __name__ == '__main__':
    app.run(port='12345')
