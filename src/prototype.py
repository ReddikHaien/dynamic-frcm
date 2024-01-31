import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form_display():
    return '''
        <form method="post">
            <input type="text" name="input1" placeholder="Input 1"/>
            <input type="text" name="input2" placeholder="Input 2"/>
            <input type="submit" value="Submit"/>
        </form>
    '''

@app.route('/', methods=['POST'])
def form_submit():
    input1 = request.form['input1']
    input2 = request.form['input2']

    # API endpoint
    api_url = 'http://127.0.0.1:5001/api/data'  # Local

    coordinates = {
        'field1': input1,
        'field2': input2
    }

    response = requests.post(api_url, json=coordinates)

    if response.status_code in [200, 201]:  # Handle both 200 OK and 201 Created
        api_response = response.json()
        return f'API Response: {api_response}'
    else:
        return f'Error calling API: Status code {response.status_code}'


if __name__ == '__main__':
    app.run(debug=True, port=5000) #FOR LOCAL
