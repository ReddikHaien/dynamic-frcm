from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Example data
    data = {"message": "Hello, world!"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    # Process the new_data as needed
    return jsonify({"message": "Data received", "received_data": new_data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001) #FOR LOCAL
