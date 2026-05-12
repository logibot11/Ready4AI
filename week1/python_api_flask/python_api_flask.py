# Autor uczący się: Jarosław Krefft
# Data utworzenia: 12.05.2026
# Nazwa i wersja programu: python_api_flask.py 
# Przykład użycia API, gdzie GET przyjmuje argumenty z URL (request.args) i filtruje dane.


from flask import Flask, jsonify, request


app = Flask(__name__)

#----------------------------------------------------------------
#      FAKE DATABASE
#----------------------------------------------------------------

users = [
    {"id":1, "name":"Yaro", "city":"Gdansk", "age":30},
    {"id":2, "name":"Stach", "city":"Lodz", "age":29},
    {"id":3, "name":"Mar", "city":"Warszawa", "age":50},
    {"id":4, "name":"Luke", "city":"Krakow", "age":31}

]

#----------------------------------------------------------------
# GET  /users (z filtrowaniem)
# --------------------------------------------------------------- 

@app.route('/users', methods=['GET'])
def get_users():
    # pobranie parametrów z url
    city = request.args.get('city')
    age = request.args.get('age')

    result = users # pełna lista

    # filtrowanie po mieście
    if city:
        result = [u for u in result if u["city"].lower() == city.lower()]

    # filtrowanie według wieku
    if age:
        try:
            age = int(age)
            result = [u for u in result if u["age"] == age]
        except ValueError:
            return jsonify(error="Age musi być liczbą"), 400
    
    # odpowiedź
    return jsonify(
        count=len(result),
        data=result
    )

# -----------------------------------------------------------------------------
# START APLIKACJI
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(port=3000, debug=True)
            
