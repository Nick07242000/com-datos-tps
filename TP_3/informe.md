# Trabajo Practico N°3

**Nombres**

- Constanza Medran  
- Fabian N Hidalgo  
- Juan I Vizgarra  
- Sofia V Castro

**Datacenter**

**Universidad Nacional de Córdoba - Facultad de Ciencias Exactas Fisicas y Naturales**  

**Comunicaciones de Datos** 

**Santiago M. Henn - Miguel Solinas** 

**08/09/2025**

---

### Información de los autores

* **Información de contacto**: *victoria.castro@mi.unc.edu.ar - fabian.hidalgo@mi.unc.edu.ar - constanza.medran@mi.unc.edu.ar - juan.vizgarra@mi.unc.edu.ar*

---

## Resumen

En este trabajo práctico se estudian las capas de acceso en redes locales, los estándares más relevantes en su desarrollo y los protocolos asociados a la transmisión de datos. 

Se analizan los estándares IEEE 802.3 (Ethernet) y 802.11 (Wi-Fi), su evolución histórica y sus diferencias clave, relacionándolos con aspectos de seguridad y compatibilidad. 

Asimismo, se introducen conceptos de transmisión óptica en fibra, destacando los modos de propagación y su relación con fenómenos físicos como la Ley de Snell. 

Se investigan también los principales protocolos de comunicación inalámbrica utilizados en la actualidad, con especial atención a su alcance, tasa de datos y aplicaciones en el ecosistema IoT. 

Finalmente, se aborda el estado del arte en conectividad aérea, explorando las tecnologías que permiten acceso a internet en vuelo y sus limitaciones.

**Palabras clave:** *IEEE 802.3, IEEE 802.11, Wi-Fi, fibra óptica, protocolos inalámbricos, IoT, comunicaciones en vuelo*

---

## Introducción

El crecimiento exponencial del tráfico de datos y la masificación de dispositivos conectados han impulsado la necesidad de contar con tecnologías de acceso eficientes, seguras y estandarizadas. 

En este marco, los organismos de normalización como el IEEE han definido protocolos que constituyen la base del funcionamiento de redes locales cableadas e inalámbricas. Comprender estas tecnologías resulta fundamental no solo para el diseño de redes modernas, sino también para anticipar los desafíos asociados a compatibilidad, seguridad y rendimiento.

Este trabajo práctico se enmarca en ese objetivo: profundizar en los fundamentos de la capa de acceso a la red mediante el estudio de los estándares IEEE 802.3 (Ethernet) y 802.11 (Wi-Fi), y la exploración de medios de transmisión como la fibra óptica y diversas tecnologías inalámbricas. 

Asimismo, se busca relacionar los fenómenos físicos de propagación con las decisiones de diseño de red, y analizar el rol de los protocolos en escenarios de aplicación actuales y emergentes, como el internet de las Cosas (IoT) y la conectividad en entornos de alta complejidad, por ejemplo, el acceso a internet en vuelos comerciales.

---

## Marco Teorico

La capa de acceso a la red integra funciones de la capa física y de la capa de enlace de datos en el modelo OSI, proporcionando los mecanismos necesarios para que los dispositivos se comuniquen en redes locales. En este contexto, los estándares del IEEE 802 han sido esenciales: IEEE 802.3 define Ethernet, el protocolo dominante en redes cableadas, caracterizado por su transmisión en tramas y por ofrecer versiones que escalan desde 10 Mbps hasta cientos de Gbps; mientras que IEEE 802.11 regula las redes inalámbricas Wi-Fi, abarcando desde la primera generación (802.11b) hasta estándares actuales como 802.11ax (Wi-Fi 6) y 802.11be (Wi-Fi 7).

Por otra parte, la fibra óptica constituye un medio de transmisión guiado que utiliza pulsos de luz para transportar información. Su funcionamiento se basa en principios de refracción interna total, descritos por la Ley de Snell, y permite alcanzar grandes distancias y anchos de banda con mínima atenuación, diferenciándose en modos de propagación (monomodo y multimodo).

En cuanto a los protocolos inalámbricos, el ecosistema actual es diverso: además de Wi-Fi, tecnologías como Bluetooth, ZigBee, LoRa o 5G ofrecen distintas combinaciones de alcance, tasa de datos y consumo energético, respondiendo a requerimientos específicos de aplicaciones en IoT, comunicaciones móviles o redes de corto alcance.

---

## Resultados

### Estandares

a. Estandares IEEE:

- 802.3: surgió en 1983 basándose en Ethernet (1973).
Este es un estándar de redes (cableadas) de área local que define las características de cableado y señalización; de nivel físico y los formatos de tramas de datos del nivel de enlace de datos del modelo OSI. 
Su primera implementación alcanzó una velocidad de  10 Mbits/s sobre coaxial grueso. Su evolución logró llegar a 100-200 Gb/s en 2018 con su versión 802.3cd. No solo lograron aumentar la velocidad sino extenderse a usar como medio también fibra óptica. 

- 802.11: estándares de conectividad inalámbrica. El WiFi se basa en él. Es una tecnología de red de área local inalámbrica (WLAN) que permite que los dispositivos digitales dentro de un área determinada se comuniquen mediante ondas de radio. 
Se lanzó al mercado en 1997. Permitía la transmisión inalámbrica de datos a velocidades de hasta 2 Mbit/s utilizando un espectro radioeléctrico de 2,4 GHz sin licencia.
Su versión más reciente (2021) llamada WiFi 6 llega a una velocidad teórica de 9,6Gbit/s.

b. La red Fcefyn tiene una versión del estándar 802.11ac (WiFi 5). Esto se puede ver al conectarse a ella e ingresar el comando netsh wlan show interfaces (en powershell Windows). Esto nos aporta mucha información de esta red.

<img width="963" height="811" alt="image" src="https://github.com/user-attachments/assets/b72623c8-6b78-404b-9cd9-f4391a0f1943" />

Esto también se podría ver con Wireshark y esta opción es más robusta ya que captura y decodifica las tramas de Beacon tramas de gestión en Wi-Fi que envía el AP periódicamente con información de la red y estándares soportados) y de asociación (tramas de gestión que se generan cuando un cliente se conecta a un AP y se usa para establecer.

c. Depende del protocolo. Si el AP utiliza un estándar nuevo y la NIC del dispositivo no lo soporta, la conexión no se puede establecer. En cambio, si el AP ofrece retrocompatibilidad, la NIC sí podrá conectarse, aunque la velocidad y las funciones estarán limitadas a las de la versión más antigua que ambos soporten.


d. El protocolo da la velocidad pero no determina directamente la seguridad, sino que condiciona qué seguridad puede usarse.

802.11ac: normalmente viene configurado solo con WPA2 o WPA3. A medida que avanza la versión del protocolo, se eleva el estándar mínimo de seguridad permitido.
Aún así se le da libertad al administrador para que decida qué seguridad implementar y en este caso se decidió por “Ninguna”. En la versión anterior (WiFi 4) usaba principalmente WPA2-PSK pero todavía permitía WPA/TKIP y WEP por compatibilidad.

<img width="947" height="651" alt="image" src="https://github.com/user-attachments/assets/3c7b36d9-7ad9-4b8c-8b0a-3fc7436f7e38" />

e. 

| Característica      | Wi-Fi 5              | Wi-Fi 6                  | Wi-Fi 7                    |
|---------------------|----------------------|--------------------------|-----------------------------|
| Versión IEEE        | 802.11ac             | 802.11ax                 | 802.11be                   |
| Tasa de datos máx.  | ~6.9 Gbps            | ~9.6 Gbps                | ~46 Gbps                   |
| Banda(s)            | 5 GHz                | 2.4 GHz y 5 GHz          | 2.4, 5 y 6 GHz             |
| Ancho de Banda      | Hasta 160 MHz        | Hasta 160 MHz            | Hasta 320 MHz              |
| Modulación          | 256-QAM              | 1024-QAM                 | 4096-QAM                   |
| Sistema de Seguridad| WPA2 (AES) o WPA3    | WPA3                     | WPA3 (base), WPA4 futuro   |

---

### Fibra Optica

2) Observar la siguiente Figura representando transmisiones en Fibra Óptica:
<img width="673" height="140" alt="image" src="https://github.com/user-attachments/assets/a15a0282-ce8f-401e-a1de-ec1401d85022" />

a) ¿Qué tipos de transmisión se están ilustrando? ¿Cuáles son sus características principales y en qué
se diferencian una de otra? 

La imagen presenta la propagación de la luz a través de una fibra óptica del tipo de transmision, fibra monomodo (izquierda) y fibra multimodo (derecha).
La imagen de la izquierda muestra un haz de luz viajando directamente a través del centro del núcleo de la fibra. Esto es típico de la fibra monomodo, que se utiliza para largas distancias y altas velocidades, ya que no hay dispersión de la señal.
La imagen de la derecha muestra la luz rebotando repetidamente en las paredes internas de la fibra a medida que avanza. Esto es característico de la fibra multimodo, que se usa para distancias más cortas. Los diferentes rayos de luz (o "modos") viajan por caminos distintos y llegan al final en momentos ligeramente diferentes, lo que provoca una dispersión modal que limita su distancia y velocidad.

¿Cuál es más costosa de implementar?
La fibra multimodo es generalmente más costosa de implementar que la monomodo, debido principalmente al alto precio de los transceptores (equipos de envío y recepción) que requiere. La fibra monomodo es más económica para largas distancias y ofrece un mejor rendimiento.

b) ¿Qué es la Ley de Snell? ¿Cómo se relaciona con las transmisiones en Fibra Óptica y sus distintos
modos?
La ley de Snell establece una relación matemática entre los ángulos de incidencia y refracción de un rayo de luz. Se expresa con la fórmula:
  n1*sin(θ1) = n2 * sin(θ2)

n1 es el índice de refracción del primer medio (donde la luz incide).
θ1 es el ángulo de incidencia.
n2 es el índice de refracción del segundo medio (donde la luz se refracta).
θ2 es el ángulo de refracción.

Cuando un rayo de luz pasa de un medio más denso (n1 alto) a uno menos denso (n2 bajo), se aleja de la normal (la línea perpendicular a la superficie de separación). Si el ángulo de incidencia es lo suficientemente grande, el rayo de luz no se refracta sino que se refleja completamente de vuelta al primer medio. Este fenómeno se conoce como reflexión interna total, y es el principio clave que hace que la fibra óptica funcione.

En una fibra óptica, el núcleo (core) tiene un índice de refracción más alto (n1) que el revestimiento (cladding) que lo rodea (n2). La Ley de Snell explica cómo la luz que entra en el núcleo en un ángulo adecuado se refleja repetidamente en la interfaz entre el núcleo y el revestimiento, permitiendo que la señal viaje a lo largo de la fibra sin escaparse.
En la Fibra Multimodo, con un núcleo de gran diámetro, permite que la luz viaje por múltiples caminos o "modos". La Ley de Snell predice que los rayos que entran con diferentes ángulos de incidencia seguirán trayectorias de distinta longitud. Esto genera dispersión modal, lo que limita la distancia y el ancho de banda.

En la Fibra Monomodo, al tener un núcleo de diámetro muy pequeño, solo permite la propagación de un único modo de luz. Esto elimina la dispersión modal, lo que hace que sea ideal para transmisiones de larga distancia y de alta velocidad.

c) ¿Qué relación podés encontrar entre las conexiones inalámbricas y las transmisiones en Fibra
Óptica?
  
La fibra óptica transporta grandes volúmenes de datos a altas velocidades a través de largas distancias. Conecta ciudades, países, centros de datos y puntos de acceso Wi-Fi. Su alta capacidad y baja latencia son fundamentales para soportar el tráfico generado por miles de usuarios.
Las conexiones inalámbricas son la interfaz que permite a los dispositivos de los usuarios (smartphones, laptops, tablets) acceder a la red. El tráfico de datos de estos dispositivos viaja a través del aire hasta un punto de acceso (por ejemplo, un router Wi-Fi o una antena 5G), que a su vez está conectado a la red troncal de fibra óptica.

---

### Protocolos
En la actualidad, la comunicación inalámbrica se ha convertido en un elemento esencial para el funcionamiento de una amplia gama de dispositivos y aplicaciones. Desde el acceso a Internet en los hogares hasta la interconexión de dispositivos en el Internet de las Cosas (IoT), los protocolos inalámbricos cumplen un papel fundamental al permitir la transmisión de datos de forma eficiente, rápida y segura.

Cada protocolo inalámbrico está diseñado para responder a necesidades específicas, ya sea en términos de alcance, velocidad de transferencia, consumo energético o tipo de aplicación. Por esta razón, no existe un protocolo único que cubra todos los escenarios, sino un conjunto de estándares que evolucionan constantemente para adaptarse a las demandas tecnológicas actuales.

A continuación, se presentan algunos de los protocolos inalámbricos más utilizados, acompañados de información sobre su estandarización y las versiones más recientes de los estándares aplicables.

| Protocolo | ¿Está estandarizado? Si/No | Si aplica: ¿Cuál(es) estándares? (si tiene varios mencionar la última versión) |
|-----------|-----------------------------|--------------------------------------------------------------------------------|
| Wi-Fi     | Sí                          | IEEE 802.11be (WiFi 7)                                                         |
| Bluetooth | Sí                          | IEEE 802.15.1 (Bluetooth 6.0)                                                  |
| ZigBee    | Sí                          | IEEE 802.15.4 (ZigBee 3.0)                                                     |
| NFC       | Sí                          | ISO/IEC 18092                                                                  |
| LTE       | Sí                          | 3GPP Release 16 (LTE Advanced Pro)                                             |
| GSM       | Sí                          | 3GPP Release 8                                                                 |
| 5G (3GPP) | Sí                          | 3GPP Release 20 (5G Advanced)                                                  |
| LoRa      | Sí (*)                      | LoRaWAN (última versión: LoRaWAN 1.1)                                          |
| NB-IoT    | Sí                          | 3GPP Release 18                                                                |
| SigFox    | No                          | No tiene estándar formal (tecnología propietaria)                              |
| Z-Wave    | No                          | No tiene estándar formal (tecnología propietaria)                              |

(*) **LoRa** en sí no es un estándar formalizado por una organización de estandarización como la ITU o el IEEE, 
sino una tecnología propietaria desarrollada por **Semtech**.  
Sin embargo, **LoRaWAN**, que es el protocolo que utiliza LoRa para la comunicación en redes, sí está estandarizado por la **LoRa Alliance**, que promueve su uso y proporciona un marco para su implementación.

Una vez identificados los estándares o la documentación correspondiente a cada tecnología, es recomendable llevar a cabo una comparación detallada de su tasa de transferencia (bit rate) y su alcance. Resulta fundamental comprender en qué aspectos sobresale cada tecnología, ya que tanto la distancia de operación en condiciones normales como la velocidad de transmisión de datos son parámetros clave a la hora de elegir la tecnología de comunicación más adecuada.

| Protocolo  | Alcance   | Tasa de Datos (máxima aproximada) |
|------------|-----------|-----------------------------------|
| NFC        | 10 [cm]   | 424 [Kbps]                        |
| Bluetooth  | 240 [m]   | 50 [Mbps]                         |
| ZigBee     | 20 [m]    | 250 [Kbps]                        |
| Z-Wave     | 100 [m]   | 100 [Kbps]                        |
| Wi-Fi      | 120 [m]   | 46 [Gbps]                         |
| GSM        | 35 [km]   | 64 [Kbps]                         |
| LTE        | 10 [km]   | 150 [Mbps]                        |
| NB-IoT     | 15 [km]   | 250 [Kbps]                        |
| LoRa       | 20 [km]   | 50 [Kbps]                         |
| SigFox     | 20 [km]   | 1000 [bps]                        |
| 5G         | 500 [m]   | 20 [Gbps]                         |

Gráfico de las características de alcance (distancia) y data rate de los protocolos mencionados:
<img width="1056" height="707" alt="Image" src="https://github.com/user-attachments/assets/bb7ff192-6b5c-477f-bc13-33e9440f0797" />

-----------------------------------

La siguiente tabla muestra una comparación entre cinco tecnologías de comunicación comunes: UTP, fibra óptica, Wi-Fi 802.11be (Wi-Fi 7), Bluetooth 5.4 y 5G. Se destacan varias características clave, como el ancho de banda, donde Wi-Fi 7 y 5G alcanzan las mayores tasas de transferencia teóricas, con 23 Gbps y 20 Gbps respectivamente, mientras que UTP y Bluetooth presentan capacidades más reducidas. La distancia de transmisión varía significativamente entre tecnologías, desde los 100 metros de UTP hasta los 100 km que puede alcanzar la fibra óptica en enlaces monomodo.

En cuanto a la inmunidad frente a interferencias electromagnéticas (EMI) y de radiofrecuencia (RFI), la fibra óptica sobresale por su alta resistencia, mientras que las tecnologías inalámbricas y UTP son más susceptibles. Cabe mencionar que la disponibilidad de estas tecnologías en Packet Tracer es limitada para las versiones más recientes; sin embargo, todas cuentan al menos con una variante básica que permite realizar simulaciones.

| Característica                    | UTP              | Fibra Óptica      | Wi-Fi 7               | Bluetooth 5.4        | 5G                        |
|-----------------------------------|------------------|-------------------|-----------------------|-----------------------|---------------------------|
| **Ancho de Banda**                | 10 Mbps - 10 Gbps| 10 Mbps - 100 Gbps| 0.4 Mbps - 23 Gbps    | 1 Mbps - 2 Mbps       | 186 Mbps - 20 Gbps        |
| **Distancias**                    | 1 - 100 m        | 1 - 100 km        | 30 - 120 m            | 240 m                 | 100 - 450 m               |
| **Inmunidad frente a EMI/RFI**    | Baja             | Más Baja          | Baja                  | Baja                  | Media                     |
| **Costos**                        | Más Bajo         | Más Alto          | Medio/Alto            | Bajo                  | Alto                      |
| **Disponibilidad en Packet Tracer** | Sí              | Sí                | No (Otras versiones sí)| No (Otras versiones sí)| No (Otras versiones sí)  |


---

### Conectividad en Aeronaves

#### Estado del Arte

El estado del arte es una revisión actualizada y sistemática de los conocimientos, desarrollos y avances más recientes sobre un tema específico. Su objetivo es mostrar qué se sabe hasta el momento, qué tecnologías o métodos existen, qué limitaciones tienen y qué tendencias futuras se están explorando.

En otras palabras, el estado del arte es “la foto actual del conocimiento y la tecnología en un área”, y se usa para fundamentar un trabajo mostrando que se conocen los avances recientes y qué lugar ocupa nuestra investigación o práctica dentro de ese panorama.

#### Tecnologias Principales

En el contexto de la conectividad a internet en aeronaves, existen actualmente dos enfoques tecnológicos principales: los sistemas satelitales y los sistemas air-to-ground (ATG).

En los sistemas satelitales, se emplean satélites geoestacionarios (GEO) y, más recientemente, constelaciones de satélites de órbita baja (LEO). Los GEO ofrecen amplia cobertura global, aunque presentan altas latencias debido a la distancia de 36.000 km. Por su parte, los LEO (como la red Starlink de SpaceX) prometen menores retardos y mayores anchos de banda, aunque requieren una infraestructura más compleja y en expansión.

Los sistemas ATG, por otro lado, se basan en antenas terrestres que transmiten hacia la aeronave mientras esta se encuentra en vuelo sobre tierra firme. Esta solución presenta baja latencia y costos reducidos, pero limita su funcionamiento a zonas continentales, quedando inoperativa en vuelos transoceánicos.

En cuanto a protocolos y estándares, la conectividad aérea se apoya en variantes optimizadas de TCP/IP y en mecanismos de gestión de calidad de servicio (QoS), con el fin de priorizar aplicaciones críticas y minimizar el impacto del retardo en servicios sensibles como videollamadas.

Actualmente, la tendencia se orienta a la integración de redes híbridas que combinan satélites LEO con enlaces ATG, buscando un equilibrio entre cobertura global, capacidad y latencia reducida. Diversos estudios proyectan que, hacia el final de la década, la disponibilidad de internet en vuelo será comparable en calidad a la de redes terrestres de banda ancha.

#### Publicacion Cientifica

Una publicacion cientifica reciente sobre esta tecnologia es [Enabling Continuous 5G Connectivity in Aircraft through Low Earth Orbit Satellites](https://arxiv.org/abs/2504.07262), el cual habla sobre estrategias de despliegue de satélites LEO para permitir conectividad 5G continua en aeronaves, considerando movimiento del avión, tránsito entre satélites, y análisis de señal dentro de la cabina mediante ray-tracing.

#### Division de Trafico

En los aviones modernos que ofrecen Wi-Fi a bordo, coexisten dos tipos de tráfico principales:

- Tráfico hacia Internet (pago):
  - Incluye navegación web, mensajería, correo electrónico, videollamadas, etc.
  - Este tráfico viaja desde el dispositivo del pasajero hacia el servidor de acceso a internet a bordo, y desde allí se envía al exterior por un enlace satelital (GEO o LEO) o air-to-ground.
  - Tiene costos asociados (ancho de banda satelital es limitado y caro), por eso suele estar tarifado para los usuarios.

- Tráfico Local (gratuito, hosteado en el avión):
  - Corresponde al sistema de entretenimiento a bordo (IFE – In-Flight Entertainment): películas, música, series, mapas interactivos, etc.
  - Este contenido está almacenado en servidores locales dentro del avión, usualmente un servidor multimedia conectado a la red interna (LAN).
  - El acceso no pasa por el satélite ni consume ancho de banda externo. Funciona similar a un servidor de streaming en una red local: el dispositivo del pasajero se conecta al servidor del avión y recibe el contenido por Wi-Fi local.

En resumen, ver una película en el sistema de entretenimiento es tráfico intra-red local, y enviar un correo es tráfico extra-red que debe salir del avión, pasando por el enlace satelital/ATG, consumiendo recursos de internet.

En Packet Tracer podriamos simular esto mediante un servidor local (representando el sistema de entretenimiento a bordo), configurar PCs representado los pasajeros al router Wi-Fi del avion, y configurar un router hacie internet (representando el enlace satelital). Asi dividimos el trafico, si los clientes acceden a una IP privada local, reciben contenido gratuito, y si acceden a una IP publica el trafico debe salir hacia internet y es tarifado.

---

## Discusión y conclusiones

---

## Referencias

[1] - Apuntes de Teoría de las Comunicaciones

[2] - Apuntes de Comunicaciones Digitales

[3] - IEEE 802.3 Ethernet Standard.
