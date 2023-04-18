from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)



def lcm(a, b):
    gcd = 0
    if a > b:
        gcd = a
    else:
        gcd = b
    while True:
        if gcd % a == 0 and gcd % b == 0:
            lcm = gcd
            break
        gcd += 1
    return lcm

@app.route('/lcm-helper')

def lcm_helper():
    number1 = int(request.args.get('param1'))
    number2 = int(request.args.get('param2'))
    result = lcm(number1,number2)
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8005)