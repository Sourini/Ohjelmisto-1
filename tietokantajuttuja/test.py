import mysql.connector


def executeSQLsearch(sql, params):
    cursor = connection.cursor()
    cursor.execute(sql, params)
    return cursor.fetchall()

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

icao = input('enter the ICAO code of the airport you are looking for: ')
sql = "select name, municipality from airport where ident =%s"

values = [icao]

result = executeSQLsearch(sql, values)
for row in result:
    print(row)