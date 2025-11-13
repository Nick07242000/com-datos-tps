import paho.mqtt.client as mqtt
import ssl, time

BROKER_URL = "af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud" # ¡REEMPLAZA!
PORT = 8883
USERNAME = "hivemq.webclient.1763039506143"
PASSWORD = "k<sZ3zPU.@%rE7h5Sa2N"
TOPIC_SUBSCRIBE = "lan/broadcast/#" # Suscrito al comodín multinivel

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Client 1 conectado. Esperando Broadcasts.")
        client.subscribe(TOPIC_SUBSCRIBE, qos=1) 

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("\n" + "=" * 40)
    print(f"[{time.strftime('%H:%M:%S')}] 📥 CLIENTE 1: ¡BROADCAST RECIBIDO!")
    print(f"Tópico: {msg.topic}")
    print(f"Mensaje: {payload}")
    print("=" * 40)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "Client1_Broadcast_Sub")
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(tls_version=ssl.PROTOCOL_TLS) 
client.on_connect = on_connect
client.on_message = on_message

if __name__ == '__main__':
    try:
        client.connect(BROKER_URL, PORT, 60)
        client.loop_forever() 
    except KeyboardInterrupt:
        print("\nCliente 1 detenido.")
        client.disconnect()