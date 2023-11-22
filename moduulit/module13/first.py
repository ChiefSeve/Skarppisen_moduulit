from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/prime/<num>')
def prime(num):
    number = int(num)
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                response = {
                    "Number": number,
                    "isPrime": False
                }
                return response
        else:
            response = {
                "Number": number,
                "isPrime": True
            }
            return response
    else:
        response = {
            "Number": number,
            "isPrime": False
        }
        return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
