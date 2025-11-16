import paho.mqtt.client as mqtt
import random
import ssl
import time

# --- Parámetros de conexión ---
BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"

def connect_mqtt():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "temperature_sensor")
    client.username_pw_set(USERNAME, PASSWORD)
    # HiveMQ Cloud usa TLS, es necesario configurarlo.
    client.tls_set(tls_version=ssl.PROTOCOL_TLS) 
    client.connect(BROKER_URL, PORT, 60)
    return client

def publish(client, room, temperature):
    result = client.publish(f"lan/sala{room}/sensor/temp", temperature, qos=1) # QoS 1 garantiza la llegada al menos una vez
    # Verifica si el mensaje fue enviado con éxito
    if result[0] == 0:
        print(f"[{time.strftime('%H:%M:%S')}] ✅ Temperatura enviada: '{temperature}'")

if __name__ == '__main__':
    try:
        client = connect_mqtt()
        client.loop_start() # Inicia un hilo de red en segundo plano
        for i in range(100):
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