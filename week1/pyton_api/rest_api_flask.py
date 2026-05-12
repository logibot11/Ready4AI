# Autor uczący się: Jarosław Krefft
# Data utworzenia: 11.05.2026
# Nazwa i wersja programu: rest_api_flask.py 
# Konfiguracja REST-owego web service, wykorzystanie biblioteki Flask
# Użycie metod GET i POST
# Zatrzymanie, wyjście z serwera CTRL+C
# Uwaga! - Do testów deweloperskich i na lokalnyn PC świadomie użyłem opcji debug=True znając zagrożenia za sobą niosące  .. poniżej wskazane.
#                                                                                                                             Flask pokazuje:
#                                                                                                                             traceback,
#                                                                                                                             linie kodu,
#                                                                                                                             nazwy plików,
#                                                                                                                             ścieżki systemowe,
#                                                                                                                             zmienne,
#                                                                                                                             fragmenty kodu.


from flask import Flask, jsonify, request

# stworzenie instancji aplikacji Flask
app = Flask(__name__)



# ENDPOINT GET
# endpoint testowy 
# http://127.0.0.1:3000/test
# ten endpoint odpowiada na zapytania GET

@app.route('/test', methods=['GET']) 
def test():
    # jsonify zmienia dane Python do formatu JSON
    return jsonify(result='to jest test',
                   status='success')

# ENDPONT POST - odbierajacy JSON
# methods = ['POST'] - endpoint odbiera dane wysłane metoda POST

@app.route('/test' , methods=['POST']) 
def test_post():

    # pobranie danych JSON z requesta
    # request = obiekt Flask reprezentujący zapytanie HTTP
    data = request.get_json()

    # walidacja - jeśli klient nie wyśle JSON otrzymamy komunikat o błędzie 400
    if not data:
        return jsonify(error="Brak JSON"), 400
    return jsonify(data), 201

# START APLIKACJI
# __name__ == "__main__":  -   warunek uruchomienia aplikacji przy bezpośrednim uruchomieniu pliku. 

# debug=True:
# - automatyczny restart po zmianie kodu
# - dokładne błędy Flask
# - tryb developerski

if __name__ == "__main__":
    app.run(port=3000, debug = True)