import paho.mqtt.client as mqtt
import random
import ssl
import time

# --- Parámetros de conexión ---
BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"
TOPIC_SUBSCRIBE = "lan/cmd/all"
SENSE = False
ON_COMMAND = "ON"
OFF_COMMAND = "OFF"

def connect_mqtt():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "temperature_sensor")
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(tls_version=ssl.PROTOCOL_TLS) 
    client.connect(BROKER_URL, PORT, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    return client

def publish(client, room, temperature):
    result = client.publish(f"lan/sala{room}/sensor/temp", temperature, qos=1) # QoS 1 garantiza la llegada al menos una vez
    # Verifica si el mensaje fue enviado con éxito
    if result[0] == 0:
        print(f"[{time.strftime('%H:%M:%S')}] ✅ Temperatura enviada: '{temperature}'")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT.")
        client.subscribe(TOPIC_SUBSCRIBE, qos=1) 
        print(f"Esperando mensajes en el tópico: {TOPIC_SUBSCRIBE}")
    else:
        print(f"Fallo de conexión, código de retorno {rc}")

def on_message(client, userdata, msg):
    global SENSE
    payload = msg.payload.decode()
    topic = msg.topic
    log_message(topic, payload)
    print(payload)
    if payload == ON_COMMAND:
        SENSE = True
    if payload == OFF_COMMAND:
        SENSE = False
 
def log_message(topic, msg):
    print("-" * 30)
    print(f"[{time.strftime('%H:%M:%S')}] 📥 MENSAJE RECIBIDO")
    print(f"Tópico: {topic}")
    print(f"Payload: {msg}")
    print("-" * 30)

if __name__ == '__main__':
    try:
        client = connect_mqtt()
        client.loop_start() # Inicia un hilo de red en segundo plano
        while (True):
            if (SENSE):
                temperature = random.randint(25, 38)
                publish(client, 1, temperature)
                temperature = random.randint(16, 23)
                publish(client, 2, temperature)
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nPublisher detenido.")
        client.loop_stop()
        client.disconnect()
    except Exception as e:
        print(f"Ocurrió un error: {e}")