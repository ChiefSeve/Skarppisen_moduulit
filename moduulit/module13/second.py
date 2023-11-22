import mysql.connector
from flask import Flask, request, Response
import json

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='flight_game'
)

my_cursor = mydb.cursor(dictionary=True, buffered=True)

app = Flask(__name__)


@app.route('/airport/<icao>')
def airport(icao):
    print(icao, 'ICAO')
    sql = f'''select ident, name, municipality
     FROM airport WHERE ident = %s'''
    my_cursor.execute(sql, (icao,))
    result = my_cursor.fetchone()
    if result:
        return result
    else:
        response = {
            'Data': 'no data'
        }
        return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
