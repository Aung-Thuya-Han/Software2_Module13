from flask import Flask, json
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='password',
    autocommit=True
)

def get_airport_info(icao):
    cursor = connection.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    if result:
        return {
            "ICAO": icao.upper(),
            "Name": result[0],
            "Location": result[1]
        }
    else:
        return None


@app.route("/airport/<icao>")
def airport_route(icao):
    data = get_airport_info(icao)
    if data:
        json_data = json.dumps(data, sort_keys=False)
        return json_data
    else:
        json_data = json.dumps(
            {"error": f"No airport found with ICAO code '{icao.upper()}'"}
        )
        return app.response_class(
            response=json_data,
            status=404,
            mimetype='application/json'
        )

if __name__ == "__main__":
    app.run(debug=True)
