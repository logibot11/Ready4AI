# Autor uczący się: Jarosław Krefft
# Data utworzenia: 11.05.2026
# Nazwa i wersja programu: rest_api_flask.py 
# Konfiguracja REST-owego web service, wykorzystanie biblioteki Flask
# Użycie metod GET i POST
# Zatrzymanie, wyjście z serwera CTRL+C


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['GET']) #endpoint GET

def test():
    return jsonify(result='to jest test')

@app.route('/test' , methods=['POST']) #endpoin 2
def test_post():
    request_data = request.get_json()

    return request_data, 201


app.run(port=3000)