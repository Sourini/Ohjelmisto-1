import mysql.connector
from flask import Flask, request

conn = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

#imported from our project because i'm lazy
def sql_query(fn, params = None):
    if params:
        query, prepared = fn(params)
    else:
        query, prepared = fn()
    cursor = conn.cursor(prepared=True, dictionary=True)
    cursor.execute(query, prepared)
    return cursor.fetchall()


def fetch_name(ident):
    sql = f"select name from airport where ident = %s"
    return sql, (ident,)
def fetch_location(ident):
    sql = f"select municipality from airport where ident = %s"
    return sql, (ident,)


app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    name = sql_query(fetch_name, icao)
    location = sql_query(fetch_location, icao)
    vastaus = {
        "ICAO": icao,
        "Name": name[0]['name'],
        "Location": location[0]['municipality']
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)