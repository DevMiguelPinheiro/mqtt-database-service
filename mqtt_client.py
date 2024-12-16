import paho.mqtt.client as mqtt


class MQTTClient:
    def __init__(self, broker_url, broker_port, topic, db_service):
        self.broker_url = broker_url
        self.broker_port = broker_port
        self.topic = topic
        self.db_service = db_service

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("[INFO] Conectado ao broker MQTT!")
            client.subscribe(self.topic)
            print(f"[INFO] Subscrito no tópico: {self.topic}")
        else:
            print(f"[ERRO] Falha ao conectar, código de retorno: {rc}")

    def on_message(self, client, userdata, msg):
        try:
            payload = msg.payload.decode("utf-8")
            print(f"[INFO] Mensagem recebida: {payload}")
            temperature = float(payload)
            self.db_service.insert_temperature(temperature)
        except ValueError as e:
            print(f"[ERRO] Mensagem inválida recebida: {msg.payload}, erro: {e}")

    def start(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        try:
            print("[INFO] Tentando conexão com o broker MQTT...")
            client.connect(self.broker_url, self.broker_port, keepalive=60)
            client.loop_forever()
        except Exception as e:
            print(f"[ERRO] Falha no serviço MQTT: {e}")
