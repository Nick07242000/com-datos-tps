import paho.mqtt.client as mqtt
import ssl, time

BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"
TOPIC_SUBSCRIBE = "lan/broadcast/#" # Suscrito al comodín multinivel

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Cliente B conectado. Esperando Broadcasts.")
        client.subscribe(TOPIC_SUBSCRIBE, qos=1) 

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("\n" + "*" * 40)
    print(f"[{time.strftime('%H:%M:%S')}] 📥 CLIENTE B: ¡BROADCAST RECIBIDO!")
    print(f"Tópico: {msg.topic}")
    print(f"Payload: {payload}")
    print("*" * 40)

# ÚNICA DIFERENCIA CLAVE: ID distinto
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Broadcast_Subscriber_B") 
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(tls_version=ssl.PROTOCOL_TLS) 
client.on_connect = on_connect
client.on_message = on_message

if __name__ == '__main__':
    try:
        client.connect(BROKER_URL, PORT, 60)
        client.loop_forever() 
    except KeyboardInterrupt:
        print("\nCliente B detenido.")
        client.disconnect()