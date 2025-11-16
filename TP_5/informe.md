 # Trabajo Practico N°5

**Nombres**

- Constanza Medran  
- Fabian N Hidalgo  
- Juan I Vizgarra  
- Sofia V Castro

**Datacenter**

**Universidad Nacional de Córdoba - Facultad de Ciencias Exactas Fisicas y Naturales**  

**Comunicaciones de Datos** 

**Santiago M. Henn - Miguel Solinas** 

**16/11/2025**

---

### Información de los autores

* **Información de contacto**: *victoria.castro@mi.unc.edu.ar - fabian.hidalgo@mi.unc.edu.ar - constanza.medran@mi.unc.edu.ar - juan.vizgarra@mi.unc.edu.ar*

---

## Resumen

En este trabajo práctico se implementa y analiza el funcionamiento del protocolo MQTT dentro de una red local simulada, empleando el modelo de comunicación Publish/Subscribe. 

Se despliega un broker MQTT —local o cloud— y se configuran múltiples clientes que actúan como dispositivos IoT, publicando y recibiendo información en distintos tópicos jerárquicos. 

Se experimenta con publicaciones directas, broadcasting mediante comodines y recolección centralizada de datos en un gateway. 

Además, se capturan paquetes de red para estudiar la estructura del protocolo y se evalúan aspectos de integridad, disponibilidad, confidencialidad y QoS. 

El objetivo final es comprender el comportamiento de sistemas IoT basados en mensajería ligera y su aplicación en arquitecturas distribuidas.

**Palabras clave:** *MQTT, IoT, publish/subscribe, broker, tópicos, QoS, mensajería ligera, simulación de red, protocolos IoT, captura de paquetes.*

---

## Introducción

El rápido crecimiento del Internet de las Cosas (IoT) ha impulsado la necesidad de protocolos de comunicación eficientes, ligeros y escalables. En este contexto, MQTT (Message Queuing Telemetry Transport) se ha consolidado como uno de los estándares más utilizados debido a su bajo consumo de ancho de banda, su simplicidad y su orientación a escenarios donde los dispositivos poseen recursos limitados.

Este trabajo práctico tiene como finalidad introducir el uso de MQTT en una red local simulada, utilizando un broker como punto central de mensajería y distintos clientes que actúan como publicadores y suscriptores. Mediante esta práctica se experimenta con tópicos jerárquicos, comodines, niveles de QoS y captura de paquetes, permitiendo observar el comportamiento real del protocolo en una arquitectura pub/sub.

Asimismo, se busca desarrollar criterios para evaluar las ventajas y limitaciones del modelo Publish/Subscribe frente al modelo cliente-servidor tradicional, especialmente en lo referido a escalabilidad, desacoplamiento, fiabilidad y seguridad. De este modo, el trabajo permite comprender los fundamentos técnicos que sustentan gran parte de las plataformas IoT modernas.

---

## Marco Teorico

### MQTT y el modelo Publish/Subscribe

MQTT (Message Queuing Telemetry Transport) es un protocolo de mensajería ligero orientado al transporte eficiente de datos entre dispositivos IoT que utiliza el patrón Publish/Subscribe (Pub/Sub). Está diseñado para funcionar sobre redes inestables o con bajo ancho de banda, lo que lo convierte en una opción ideal para sensores, actuadores y sistemas embebidos.

### Broker MQTT

El broker actúa como intermediario en la comunicación y es responsable de gestionar las suscripciones, recibir y reenviar mensajes, aplicar los niveles de QoS, mantener sesiones persistentes, controlar permisos y autenticación.

### Tópicos, Jerarquías y Comodines

Los tópicos representan canales lógicos de comunicación y están organizados en estructuras jerárquicas (por ejemplo: lan/sala1/sensor/temp). MQTT permite:
- Comodín “+” → Matchea un nivel único de la jerarquía.
- Comodín “#” → Matchea todos los niveles inferiores.

Esto facilita la implementación de broadcast y routing lógico dentro de una red.

### QoS – Quality of Service

MQTT define tres niveles de fiabilidad:
- QoS 0: "At most once" – sin confirmación.
- QoS 1: "At least once" – recibe confirmación, puede haber duplicados.
- QoS 2: "Exactly once" – evita duplicados, mayor costo.

El nivel de QoS seleccionado influye directamente en la confiabilidad de la comunicación y en la carga del broker.

---

## Resultados
 
### Características de MQTT

Protocolo: Message Queuing Telemetry Transport (MQTT).

Diseño: Es un protocolo de mensajería ligero, diseñado para dispositivos con recursos limitados y redes de baja calidad (alto latencia/bajo ancho de banda).

Modelo: Sigue el patrón Publish/Subscribe (Pub/Sub).

Ventajas: Bajo consumo de energía, uso eficiente del ancho de banda, baja sobrecarga (overhead), confiabilidad definida por niveles de QoS.

Desventajas: Dependencia de un broker central, no está diseñado para el intercambio de grandes volúmenes de datos.

Usos Principales: Internet de las Cosas (IoT), telemetría, sistemas de monitoreo y control remoto, aplicaciones móviles.

#### ¿Qué es el patrón de diseño Pub/Sub?

Es un modelo de comunicación asíncrona donde los remitentes de los mensajes (Publishers) no se programan para enviar sus mensajes a receptores específicos.

En este patron los mensajes son publicados en categorías conocidas como tópicos y los receptores (Subscribers) expresan interés en uno o más tópicos. 

Un componente intermedio (Broker) filtra los mensajes según los tópicos y los distribuye a los Subscribers.

Se diferencia del modelo tradicional Cliente-Servidor en que el remitente y el receptor no tienen conocimiento directo entre sí (desacoplamiento)

### Instalar y Ejecutar un Broker

Configuramos y ejecutamos un broker MQTT con HiveMQ:

<img width="1312" height="578" alt="image" src="https://github.com/user-attachments/assets/b07b401e-1a70-4245-8d6a-842e3f2b406e" />
<img width="689" height="564" alt="image" src="https://github.com/user-attachments/assets/0fd88cdc-48a4-409a-a270-c133f39ef7c4" />

Para el cual tenemos los siguientes detalles de la conexión:
- URL: af2472e326aa4722936e47e029e3d7ed.s1.eu.hivemq.cloud 
- Port: 8883 
- WebSocket Port: 8884 

Estos datos son los necesarios para que tus clientes se conecten al broker.

### Verificar Funcionamiento (Conexión Cliente)

Instalamos un cliente MQTT en python y lo conectamos al broker, intentado suscribirnos a un tópico y publicar un mensaje para confirmar que el broker lo recibe y lo reenvía.

<img width="1363" height="704" alt="Captura de pantalla 2025-11-13 104659" src="https://github.com/user-attachments/assets/88783e17-6b18-41d3-a15d-72a0ef5c496c" />

En la imagen podemos observar un cliente web conectado (The WebClient is connected) y recibiendo un mensaje en el tópico test.

### Arquitectura Funcional

#### Comunicación Directa (Punto a Punto simulado):

- Creamos el Dispositivo A que publica en el tópico lan/deviceA/status.
- Creamos el Dispositivo B que se suscribe al tópico lan/deviceA/status y muestra los mensajes.

<img width="1300" height="297" alt="image" src="https://github.com/user-attachments/assets/36c675cd-718e-4eb6-9fb9-6c5e29e0c7d0" />
<img width="1363" height="698" alt="image" src="https://github.com/user-attachments/assets/e7fa13e3-bcd3-4c79-abbf-a2fa903dab70" />

#### Broadcasting:

- Creamos el tópico general lan/broadcast/# (el # es un comodín de múltiples niveles).
- Configuramos dos clientes para suscribirse a lan/broadcast/#.
- Desde un cliente "central", publicamos mensajes en lan/broadcast/all.
- Ambos clientes suscritos a lan/broadcast/# reciben el mensaje publicado en lan/broadcast/all.

<img width="1296" height="297" alt="image" src="https://github.com/user-attachments/assets/3a6f0a7e-a4a2-4db9-bdbb-a5213eaf3a11" />
<img width="1414" height="777" alt="image" src="https://github.com/user-attachments/assets/87f388a7-e6e9-47ff-b02d-9a55d82baf59" />
<img width="1416" height="778" alt="image" src="https://github.com/user-attachments/assets/a9564b0c-9905-414b-9b72-fed651cc6bcd" />


### Jerarquia de Topicos

A continuacion implementamos una jerarquia de topicos para registrar datos (simulados) de temperatura y humedad en distintas salas:
- lan/sala1/sensor/temp
- lan/sala2/sensor/temp
- lan/sala1/sensor/hum
- lan/sala2/sensor/hum

Para esto generamos publishers que simulan sensores que toman datos de temperatura o humedad y los publican a su topico correspondiente, particularmente:
- temperature_sensor: lan/sala1/sensor/temp
- temperature_sensor: lan/sala2/sensor/temp
- humidity_sensor: lan/sala1/sensor/hum
- humidity_sensor: lan/sala2/sensor/hum

Estos datos son recibidos en un gateway que obtiene los datos de todas las salas y todos los sensores, para lo cual nos subscribimos al topico jerarquico:
- lan/+/sensor/+

Este gateway registra los datos en un csv para su posterior visualizacion en [Grafana](https://fabianhidalgo.grafana.net/d/famhsmg/tp5?dashboardLibraryDatasourceUid=df4b9l3bvak8wc&orgId=1&from=2025-11-16T13:19:09.941Z&to=2025-11-16T13:20:22.943Z&timezone=browser&tab=transformations&editPanel=1).

<img width="2208" height="591" alt="image" src="https://github.com/user-attachments/assets/fc18f7e7-52de-493c-8867-260e0ab97aad" />

Luego, agregamos el accionado de los sensores por comando. Para lograr esto cada sensor se subscribe a un topico de broadcast para escuchar comandos, y solo comienzar a sensar al recibir el command ON, finalizando al recibir OFF:

<img width="1357" height="609" alt="image" src="https://github.com/user-attachments/assets/c2f275c7-8448-4fc5-8c59-1d5ba0d1de49" />
<img width="1050" height="438" alt="image" src="https://github.com/user-attachments/assets/2bc2fde8-f2bc-4c2f-855c-f7838ae751cc" />
<img width="1458" height="761" alt="image" src="https://github.com/user-attachments/assets/4a9383eb-f4b1-4abe-80d7-a14239f10c9a" />
<img width="1426" height="756" alt="image" src="https://github.com/user-attachments/assets/10d314bc-7a5f-40a2-8b3d-12663a1678ff" />

Puede observarse que despues de enviar OFF, se terminar de procesar los mensajes que estaban en el topico, pero los clientes ya no envian mas.

Finalmente, analizamos un paquete enviado usando el protocolo MQTT TLS capturado con Wireshark:

<img width="2283" height="1232" alt="image" src="https://github.com/user-attachments/assets/aa3a3509-5031-4ab2-be7f-9d9ae5654d3a" />

El paquete analizado (Frame 39) corresponde a tráfico MQTT asegurado con TLS (puerto TCP 8883). 
La captura muestra un paquete TCP (PSH,ACK) de 33 bytes de payload, transportando un registro TLSv1.2 de 28 bytes. 
Debido al cifrado TLS no es posible extraer el tópico ni el contenido del mensaje MQTT; únicamente puede documentarse la cabecera Ethernet/IP/TCP, el tamaño del registro TLS y las métricas temporales.
El protocolo de la capa de transporte es TCP, pudiendo apreciarse ACKs en la imagen, y el protocolo de la capa de aplicación es TLS sobre MQTT, por esto se observa TLSv1.X en los paquetes capturados, donde el trafico es envuelto en la capa de cifrado TLS.

### Q&A

a) En esta actividad, se trabaja principalmente con TCP (Protocolo de Control de Transmisión), el protocolo de capa de transporte estándar sobre el que opera MQTT.
MQTT utiliza TCP/IP en el puerto 8883 para conexiones seguras mediante TLS/SSL, asegurando una comunicación confiable, orientada a conexión, con entrega ordenada y sin pérdidas de paquetes.

b)

- Integridad: se apoya principalmente en la capa de transporte (TCP), y cuando se usa TLS, en los mecanismos criptograficos de TLS que detectan manipulaciones. TCP incorpora sumas de comprobación que detectan corrupción de paquetes en tránsito y los niveles de QoS (1 y 2) aportan confirmaciones y retransmisión a nivel MQTT, reduciendo la probabilidad de que un mensaje válido se pierda o quede corrupto. Sin protección TLS, un atacante con acceso a la red podría modificar mensajes antes de que lleguen al broker.

- Confidencialidad: se logra cifrando la conexión cliente–broker con TLS. Con TLS activo, el contenido de los mensajes y las credenciales quedan protegidos frente a escuchas pasivas. Si no hay TLS, los mensajes viajan en texto plano y pueden ser leídos por cualquier agente con acceso a la red.

- Disponibilidad: depende en gran medida del broker: al ser el punto central por donde pasa todo el tráfico MQTT, su caída interrumpe la comunicación entre dispositivos.

c) Rol de los niveles de QoS en la fiabilidad:

- QoS 0: envío sin acuse, rápido y con bajo overhead, pero no existe garantía de entrega además de la fiabilidad que ofrece TCP en la conexión. 

- QoS 1: el emisor exige confirmación(PUBACK), garantiza que el mensaje llegará al menos una vez, pero pueden producirse duplicados. 

- QoS 2: utiliza un protocolo de cuatro pasos para asegurar que el mensaje se entregue exactamente una vez, evitando duplicados, esto añade latencia y coste computacional. 


d) Ventajas del modelo pub/sub frente al cliente-servidor:

- Desacoplamiento: los productores no necesitan conocer a los consumidores (ni sus direcciones ni su estado), lo que simplifica la evolución y escalado del sistema.
- Escalabilidad y difusión eficiente: un único mensaje publicado puede entregarse a muchos suscriptores mediante el broker.
- Asincronía y tolerancia a desconexiones: los clientes pueden publicar o suscribirse sin que ambos estén activos al mismo tiempo.
- Flexibilidad en enrutamiento lógico: tópicos jerárquicos y comodines permiten seleccionar subsets de mensajes sin reconfigurar el sistema.


e) Limitaciones de MQTT respecto a una red LAN real

- Centralización: la necesidad de un broker introduce un nodo de coordinación que no existe en una comunicación punto a punto típica de una LAN, la comunicación entre dispositivos pasa por el broker en lugar de usar enlaces directos.
- No aprovecha multicast L2/L3 nativo: el “broadcast” lógico se realiza por el broker, no por mecanismos de la red local, por lo que no sustituye a servicios que dependen de multicast físico.
- Escalabilidad para grandes volúmenes o ficheros: MQTT está optimizado para mensajes pequeños, para transferencias pesadas (vídeo, archivos grandes) no es eficiente.
- Visibilidad de la red: MQTT abstrae detalles de la red subyacente (p. ej. rutas, switching), por lo que no refleja comportamientos específicos de una LAN real.
- Seguridad por configuración: la protección real depende de habilitar TLS, autenticación y ACLs, sin configuración adecuada queda expuesto, incluso en una LAN.

f) Implicaciones de depender de un broker central:

Depender de un broker central implica varias consecuencias operativas y de seguridad: el broker se convierte en un punto único de falla y, si no se dimensiona o replica adecuadamente, puede ser también un cuello de botella que limite el rendimiento del sistema. Esta centralización concentra credenciales, políticas y mensajes, de modo que una vulneración del broker compromete la confidencialidad e integridad de gran parte de la plataforma. Por otro lado, la existencia de un broker facilita la aplicación de controles centralizados (autenticación, ACLs, logging y auditoría), pero exige mantenimiento, monitorización y planes claros de recuperación ante fallos, de lo contrario, la pérdida del broker puede provocar interrupciones significativas y pérdida de mensajes si no existe persistencia.

---

## Discusión y conclusiones
Este trabajo mostró que MQTT es una solución efectiva para recolectar telemetría y controlar sensores en arquitecturas IoT ligeras: el modelo pub/sub facilita el desacoplamiento, la difusión eficiente y la tolerancia a desconexiones. Los niveles de QoS permiten ajustar la fiabilidad según la criticidad de los mensajes, y TLS asegura confidencialidad e integridad en tránsito si está bien configurado. La principal limitación es la dependencia de un broker central, que exige diseñar redundancia y buenas prácticas de seguridad y monitoreo para uso en producción.


---

## Referencias

- [Cisco Networking Academy. (2023). Introduction to Networks (Version 7.0) – Course Booklet. Cisco Press.]  (https://www.netacad.com/courses/ccna-introduction-networks)
- [PUB/SUB](https://ably.com/topic/pub-sub)
- [MQTT](https://www.geeksforgeeks.org/computer-networks/introduction-of-message-queue-telemetry-transport-protocol-mqtt/)