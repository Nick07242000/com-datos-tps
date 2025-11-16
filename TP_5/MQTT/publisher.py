import paho.mqtt.client as mqtt
import ssl
import time

# --- Parámetros de conexión ---
BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"
STATUS_TOPIC = "lan/deviceA/status"
BROADCAST_TOPIC = "lan/broadcast/all"

def connect_mqtt():
    """Conecta el cliente usando TLS y credenciales."""
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "DeviceA_Publisher")
    client.username_pw_set(USERNAME, PASSWORD)
    # HiveMQ Cloud usa TLS, es necesario configurarlo.
    client.tls_set(tls_version=ssl.PROTOCOL_TLS) 
    client.connect(BROKER_URL, PORT, 60)
    return client

def publish(client, topic, message):
    """Publica mensaje al topico especificado."""
    result = client.publish(topic, message, qos=1) # QoS 1 garantiza la llegada al menos una vez
    # Verifica si el mensaje fue enviado con éxito
    if result[0] == 0:
        print(f"[{time.strftime('%H:%M:%S')}] ✅ Mensage enviado: '{message}'")

if __name__ == '__main__':
    try:
        client = connect_mqtt()
        client.loop_start() # Inicia un hilo de red en segundo plano
        for i in range(5):
            publish(client, STATUS_TOPIC, "STATUS: alive") # Publica status update
            publish(client,  BROADCAST_TOPIC, f"BROADCAST: Alerta general Nº {i}") # Publica broadcast
            time.sleep(3) # Espera 3 segundos
    except KeyboardInterrupt:
        print("\nPublisher detenido.")
        client.loop_stop()
        client.disconnect()
    except Exception as e:
        print(f"Ocurrió un error: {e}")