import json
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load city data from JSON file
with open('cities.json', 'r') as json_file:
    city_data = json.load(json_file)

# Create a dictionary to easily look up cities by name
city_lookup = {city['city']: city for city in city_data}

@app.route('/get_firerisk_city', methods=['GET'])
def get_city_data():
    city_name = request.args.get('city')
    if city_name and city_name in city_lookup:
        city_info = city_lookup[city_name]
        lat = city_info.get('lat')
        lng = city_info.get('lng')
        return jsonify({"message": "Data received", "city": city_name, "lat": lat, "lng": lng}), 200
    else:
        return jsonify({"message": "City not found"}), 404

@app.route('/get_firerisk_coordinates', methods=['GET'])
def get_coords_data():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    return jsonify({"message": "Data received", "lat": lat, "lng": lng}), 200



if __name__ == '__main__':
    app.run(debug=True, port=5001) #FOR LOCAL
