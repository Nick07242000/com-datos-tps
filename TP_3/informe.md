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

Finalmente, se aborda el estado del arte en conectividad aérea, explorando las tecnologías que permiten acceso a Internet en vuelo y sus limitaciones.

**Palabras clave:** *IEEE 802.3, IEEE 802.11, Wi-Fi, fibra óptica, protocolos inalámbricos, IoT, comunicaciones en vuelo*

---

## Introducción

El crecimiento exponencial del tráfico de datos y la masificación de dispositivos conectados han impulsado la necesidad de contar con tecnologías de acceso eficientes, seguras y estandarizadas. 

En este marco, los organismos de normalización como el IEEE han definido protocolos que constituyen la base del funcionamiento de redes locales cableadas e inalámbricas. Comprender estas tecnologías resulta fundamental no solo para el diseño de redes modernas, sino también para anticipar los desafíos asociados a compatibilidad, seguridad y rendimiento.

Este trabajo práctico se enmarca en ese objetivo: profundizar en los fundamentos de la capa de acceso a la red mediante el estudio de los estándares IEEE 802.3 (Ethernet) y 802.11 (Wi-Fi), y la exploración de medios de transmisión como la fibra óptica y diversas tecnologías inalámbricas. 

Asimismo, se busca relacionar los fenómenos físicos de propagación con las decisiones de diseño de red, y analizar el rol de los protocolos en escenarios de aplicación actuales y emergentes, como el Internet de las Cosas (IoT) y la conectividad en entornos de alta complejidad, por ejemplo, el acceso a Internet en vuelos comerciales.

---

## Marco Teorico

La capa de acceso a la red integra funciones de la capa física y de la capa de enlace de datos en el modelo OSI, proporcionando los mecanismos necesarios para que los dispositivos se comuniquen en redes locales. En este contexto, los estándares del IEEE 802 han sido esenciales: IEEE 802.3 define Ethernet, el protocolo dominante en redes cableadas, caracterizado por su transmisión en tramas y por ofrecer versiones que escalan desde 10 Mbps hasta cientos de Gbps; mientras que IEEE 802.11 regula las redes inalámbricas Wi-Fi, abarcando desde la primera generación (802.11b) hasta estándares actuales como 802.11ax (Wi-Fi 6) y 802.11be (Wi-Fi 7).

Por otra parte, la fibra óptica constituye un medio de transmisión guiado que utiliza pulsos de luz para transportar información. Su funcionamiento se basa en principios de refracción interna total, descritos por la Ley de Snell, y permite alcanzar grandes distancias y anchos de banda con mínima atenuación, diferenciándose en modos de propagación (monomodo y multimodo).

En cuanto a los protocolos inalámbricos, el ecosistema actual es diverso: además de Wi-Fi, tecnologías como Bluetooth, ZigBee, LoRa o 5G ofrecen distintas combinaciones de alcance, tasa de datos y consumo energético, respondiendo a requerimientos específicos de aplicaciones en IoT, comunicaciones móviles o redes de corto alcance.

---

## Resultados

### Estandares

Respuestas punto 1

---

### Fibra Optica

Respuestas punto 2

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

Gráfico de las características de alcance (distancia) y data rate de los protocolos mencionados.

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


-----------------------------------
### Estado del Arte

Respuestas punto 4

---

## Discusión y conclusiones

---

## Referencias

[1] - Apuntes de Teoría de las Comunicaciones

[2] - Apuntes de Comunicaciones Digitales

[3] - IEEE 802.3 Ethernet Standard.
