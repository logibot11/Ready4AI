# Autor uczący się: Jarosław Krefft
# Data utworzenia: 11.05.2026
# Nazwa i wersja programu: rest_api_flask.py 
# Konfiguracja REST-owego web service, wykorzystanie biblioteki Flask
# Użycie metod GET i POST
# Zatrzymanie, wyjście z serwera CTRL+C

# dodanie opcji Debug włącza: debugger,
# automatyczny restart, szczegółowe błędy.

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/test', methods=['GET']) #endpoint GET
def test():
    return jsonify(result='to jest test')


@app.route('/test' , methods=['POST']) #endpoin 2
def test_post():
    data = request.get_json()

    if not data:
        return jsonify(error="Brak JSON"), 400
    return jsonify(data), 201

app.run(port=3000, debug = True)