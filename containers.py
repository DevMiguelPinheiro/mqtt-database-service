from dependency_injector import containers, providers
from config import Config
from database import Database
from mqtt_client import MQTTClient


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_dict({
        "broker_url": Config.BROKER_URL,
        "broker_port": Config.BROKER_PORT,
        "mqtt_topic": Config.MQTT_TOPIC,
        "db_host": Config.DB_HOST,
        "db_user": Config.DB_USER,
        "db_password": Config.DB_PASSWORD,
        "db_name": Config.DB_NAME,
    })

    # Serviço de Banco de Dados
    db_service = providers.Factory(
        Database,
        host=config.db_host,
        user=config.db_user,
        password=config.db_password,
        database=config.db_name,
    )

    # Cliente MQTT
    mqtt_service = providers.Factory(
        MQTTClient,
        broker_url=config.broker_url,
        broker_port=config.broker_port,
        topic=config.mqtt_topic,
        db_service=db_service,
    )
