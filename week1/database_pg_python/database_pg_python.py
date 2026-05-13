# Autor uczący się: Jarosław Krefft
# Data utworzenia: 13.05.2026
# Nazwa i wersja programu: database_pg_python.py.py 
# Program pokazujący połączenie z baza Postgres i uzycie zapytania SELECT w kodzie Python

import psycopg2
import getpass

try:
    #pobranie hasła od użytkownika - hasło 'root'
    password = getpass.getpass()

    # connection string
    conn = psycopg2.connect(
        host="localhost",
        database="virtualfactory",
        user="postgres",
        password=password
    )


    cursor = conn.cursor()
     # zapytanie SQL
    cursor.execute('SELECT "idStatus", status, description FROM production_status') # w przypadku nazw z dużej litery w nazwie kolumny stosować cudzysłów 

    # fetchall() - Metoda biblioteki psycopg2, która:
    # pobiera wszystkie rekordy zwrócone przez ostatnie SELECT,
    # zwraca je jako listę krotek (list[tuple]).
    rows = cursor.fetchall()

    # wyświetlenie wyników
    for row in rows:
        print(row)

except Exception as e:
    print("Błąd:", e)

finally:
    # zamknięcie połączeń
    # locals() to wbudowana funkcja Pythona zwracająca słownik wszystkich lokalnych zmiennych dostępnych w danym miejscu programu: cur i conn
    if 'cur' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()


