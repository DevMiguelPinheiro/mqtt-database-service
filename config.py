class Config:
    # Configurações do Broker MQTT
    BROKER_URL = "broker_mqtt.com"
    BROKER_PORT = 1883
    MQTT_TOPIC = "sensor/temperature"

    # Configurações do Banco de Dados MySQL
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWORD = "senha"
    DB_NAME = "temperature_db"
