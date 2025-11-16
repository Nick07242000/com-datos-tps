import paho.mqtt.client as mqtt
import ssl
import time

# --- Parámetros de conexión ---
BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"
TOPIC_SUBSCRIBE = "lan/deviceA/status"

def on_connect(client, userdata, flags, rc):
    """Callback que se llama al conectarse al broker."""
    if rc == 0:
        print("Conectado al broker MQTT.")
        # Una vez conectado, el Dispositivo B se suscribe al tópico de A
        client.subscribe(TOPIC_SUBSCRIBE, qos=1) 
        print(f"Esperando mensajes en el tópico: {TOPIC_SUBSCRIBE}")
    else:
        print(f"Fallo de conexión, código de retorno {rc}")

def on_message(client, userdata, msg):
    """Callback que se llama cuando se recibe un mensaje."""
    payload = msg.payload.decode()
    print("-" * 30)
    print(f"[{time.strftime('%H:%M:%S')}] 📥 MENSAJE RECIBIDO")
    print(f"Tópico: {msg.topic}")
    print(f"Payload: {payload}")
    print("-" * 30)

# Configuración del Cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Status_Subscriber")
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(tls_version=ssl.PROTOCOL_TLS) 

# Asignar funciones callback
client.on_connect = on_connect
client.on_message = on_message

if __name__ == '__main__':
    try:
        client.connect(BROKER_URL, PORT, 60)
        # El loop de red se mantiene escuchando en primer plano
        client.loop_forever() 
    except KeyboardInterrupt:
        print("\nSubscriber detenido.")
        client.disconnect()
    except Exception as e:
        print(f"Ocurrió un error: {e}")