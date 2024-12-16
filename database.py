import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def insert_temperature(self, temperature):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO temperature_readings (temperature) VALUES (%s)"
                cursor.execute(query, (temperature,))
                connection.commit()
                print(f"[INFO] Temperatura {temperature} registrada no banco de dados.")
        except Error as e:
            print(f"[ERRO] Falha ao inserir dados no banco: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
