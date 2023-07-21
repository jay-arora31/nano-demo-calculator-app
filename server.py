from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = json.loads(request.data)
    number1 = data['first']
    number2 = data['second']
    result = number1 + number2
    return result

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = json.loads(request.data)
    number1 = data['first']
    number2 = data['second']
    result = number1 - number2
    return result


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')