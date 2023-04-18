from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

@app.route('/gcd-helper')

def gcd_helper():
    number1 = int(request.args.get('param1'))
    number2 = int(request.args.get('param2'))
    result = gcd(number1,number2)
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004)