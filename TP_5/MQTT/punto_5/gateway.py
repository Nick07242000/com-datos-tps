import paho.mqtt.client as mqtt
import pandas as pd
import ssl
import time
import os

# --- Parámetros de conexión ---
BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"
TOPIC_SUBSCRIBE = "lan/+/sensor/+"
CSV_FILE = "mqtt_log.csv"

# --- Crear CSV con headers si no existe ---
def init_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["timestamp", "room", "sensor", "measurement"])
        df.to_csv(CSV_FILE, index=False)
        print(f"Archivo CSV creado con headers: {CSV_FILE}")
    else:
        print(f"Archivo CSV detectado: {CSV_FILE}")

# --- Funciones callback ---

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT.")
        client.subscribe(TOPIC_SUBSCRIBE, qos=1) 
        print(f"Esperando mensajes en el tópico: {TOPIC_SUBSCRIBE}")
    else:
        print(f"Fallo de conexión, código de retorno {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    log_message(topic, payload)
    save_message(topic, payload)
    
def log_message(topic, msg):
    print("-" * 30)
    print(f"[{time.strftime('%H:%M:%S')}] 📥 MENSAJE RECIBIDO")
    print(f"Tópico: {topic}")
    print(f"Payload: {msg}")
    print("-" * 30)

def save_message(topic, msg):
    new_row = {
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
        "room": topic.split("/")[1].replace("sala", ""),
        "sensor": topic.split("/")[3] ,
        "measurement": msg
    }
    df = pd.DataFrame([new_row])
    df.to_csv(CSV_FILE, mode='a', header=False, index=False)

# Configuración del Cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "gateway")
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(tls_version=ssl.PROTOCOL_TLS) 

# Asignar funciones callback
client.on_connect = on_connect
client.on_message = on_message

if __name__ == '__main__':
    init_csv()
    try:
        client.connect(BROKER_URL, PORT, 60)
        # El loop de red se mantiene escuchando en primer plano
        client.loop_forever() 
    except KeyboardInterrupt:
        print("\nSubscriber detenido.")
        client.disconnect()
    except Exception as e:
        print(f"Ocurrió un error: {e}")