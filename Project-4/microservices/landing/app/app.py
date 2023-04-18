SSfrom flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'



def is_numeric(string):
    # Set of valid characters for numeric values
    valid_chars = set('0123456789.')

    # Set of characters in the string
    string_chars = set(string)

    # Return True if the string consists only of valid characters
    return string_chars.issubset(valid_chars)

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    if(number_1 and number_2):

        if(is_numeric(number_1) and is_numeric(number_1)):
            number_1 = int(number_1)
            number_2 = int(number_2)

        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            response = requests.get(f'http://microservices-add-service-1:8000/add-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')
        elif operation == 'minus':
            response = requests.get(f'http://microservices-subtract-service-1:8001/subtract-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')
        elif operation == 'multiply':
            response = requests.get(f'http://microservices-multiply-service-1:8002/multiply-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')
        elif operation == 'divide':
            response = requests.get(f'http://microservices-divide-service-1:8003/divide-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')
        elif operation == 'gcd':
            response = requests.get(f'http://microservices-gcd-service-1:8004/gcd-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')
        elif operation == 'lcm':
            response = requests.get(f'http://microservices-lcm-service-1:8005/lcm-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')
        elif operation == 'modulus':
            response = requests.get(f'http://microservices-modulus-service-1:8006/modulus-helper?param1={number_1}&param2={number_2}')
            result = response.content.decode('utf-8')

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )