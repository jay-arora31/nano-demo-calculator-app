from flask import Flask, jsonify, request
import requests
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return jsonify({"message":"Hello World!"})

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Both number1 and number2 are required.'}), 400
    number1 = data['first']
    number2 = data['second']
    result = number1 + number2

    return jsonify({'result': result}),200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if 'first' not in data or 'second' not in data:
        return jsonify({'error': 'Both number1 and number2 are required.'}), 400
    number1 = data['first']
    number2 = data['second']
    result = number1 - number2

    return jsonify({'result': result}),200


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')