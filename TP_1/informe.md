# Título

**Nombres**  
- Constanza Medran
- Fabian N Hidalgo
- Juan I Vizgarra
- Sofia V Castro

**Datacenter**

**Universidad Nacional de Córdoba - Facultad de Ciencias Exactas Fisicas y Naturales**  
**Comunicaciones de Datos**
**TBD**
**TBD**

---

### Información de los autores

* **Información de contacto**: *correo electrónico*

---

## Resumen

En este trabajo se repasan los fundamentos esenciales de las comunicaciones digitales y de la teoría de las comunicaciones, estableciendo un vínculo entre la capa física y los modelos de transmisión/recepción de datos.

Asimismo, se introduce el uso del simulador Cisco Packet Tracer como herramienta para el diseño y análisis de redes.

Se abordan conceptos de ondas electromagnéticas, modulación y demodulación, señales de tiempo continuo y discreto, además de la implementación y configuración básica de una red simple con conexión cableada e inalámbrica.

Finalmente, se analizan fenómenos de propagación y su relación con las frecuencias de operación de los dispositivos.

**Palabras clave**: *comunicaciones digitales, modulación, capa física, Packet Tracer*

---

## Introducción

El presente trabajo tiene como objetivo integrar conocimientos previos de comunicaciones digitales, enfocándose en la relación entre la teoría y su aplicación práctica mediante el simulador Cisco Packet Tracer.

La comprensión de los fenómenos físicos que gobiernan la propagación de ondas electromagnéticas, junto con el conocimiento de técnicas de modulación y estructuras de señales, resulta esencial para el diseño y análisis de redes de datos.

En la primera parte, se realiza un repaso de los fundamentos esenciales: ondas electromagnéticas, procesos de modulación y demodulación, y representación de señales en tiempo continuo y discreto. 

En la segunda parte, se analiza un sistema digital desde la perspectiva de su direccionalidad, su codificación y las implicancias en velocidad y bidireccionalidad. 

Posteriormente, se estudian aspectos prácticos de modulación digital, se discuten limitaciones de la transmisión inalámbrica de señales escalonadas, y se evalúa el rendimiento mediante métricas como la tasa de error de bit (BER). 

Finalmente, se implementa en Packet Tracer una red simple para evaluar la configuración de dispositivos y las características de las señales.

---

# Marco teórico / Modelo / Metodología

## Fundamentos esenciales

Se realiza un repaso de los siguientes conceptos teóricos:

* **Ondas electromagnéticas**: ...
* **Modulación y demodulación**: ...
* **Señales en tiempo continuo**: ...
* **Señales en tiempo discreto**: ...

### Análisis de Fenómenos y Espectro Electromagnético

Dada la siguiente onda electromagnética:

_imagen del grafico - se inserta en Github_

_explicacion de como sacamos estos datos_

| Parámetro        | Valor estimado | Unidad |
| ---------------- | -------------- | ------ |
| Frecuencia       | ...            | Hz     |
| Longitud de onda | ...            | m      |

_en que region opera esta onda y en que banda + que dispositivos para comunicaciones de datos operan en esta banda_

_fenonemenos de la linea roja + afectaciones al dispositivos de ejemplos + afectaciones a transmiciones de telefonia/cable.coaxial/fibra.optica_

---

## Análisis de Sistemas Digitales

Comunicar datos a través de cualquier medio es, en esencia, un proceso que consiste en modificar el comportamiento de una señal en el tiempo.

En esta materia nos concentramos en la transmisión de datos, hoy por hoy, dominado por las señales digitales.

En el siguiente sistema:

_imagen del sistema - Github insert_

_explicacion de tipo y modo de transmision_

_justificacion del paradigma (sea o no el mejor)_

### Representación UART y codificación de caracteres

Teniendo en cuenta que en la expresión más simple de señal digital, podemos pensar que un nivel de tensión “1” representa un 1 digital, y un nivel de tensión “0” representa un 0 digital.

Si quisieramos transmitir la cuarta letra del nombre del grupo 'a' en codificacion ASCII, la señal se veria de la forma:

_grafico UART_

Teniendo en cuenta los niveles de tension al pasar de 0 a 1 o viceversa _En qué marcas temporales medirían la señal para determinar el valor digital de la misma_

---

## Limitaciones de Transmisión Inalámbrica de Señales Escalonadas

_Investigar y resumir brevemente los motivos por los cuales no es conveniente transmitir de manera inalámbrica una señal escalonada_

Es por esto que existen otras tecnicas de modulacion como: _la tecnica del grafico_

_paint de como ser veria la señal digital modulada_

_otras técnicas de modulación basadas en los mismos principios_

Un termino importante en la modulacion de señales es BER _definicion + cual tecnica es mejor_ 

---

## Implementación en Packet Tracer

Se implementó una red simple compuesta por un router inalámbrico, una computadora de escritorio conectada mediante cable y una notebook conectada vía Wi-Fi.

### Configuración de Router

<img  width="500" src="https://github.com/user-attachments/assets/bc0b0dd3-f1a3-4f79-baed-26e70b65b0f7" />

<img  width="500" src="https://github.com/user-attachments/assets/858a8662-8584-43a2-8c80-e09151ae35d2" />

Los parámetros básicos configurados fueron:

* Dirección IP del router: 192.168.0.1
* Máscara de subred: 255.255.255.0
* SSID: Virus
* Seguridad:
  - WPA2-PSK
  - PSK Pass Phrase 3161341211620
  - Encriptación: AES

El router opera en una frecuencia de 2.4 GHz, perteneciente a la región de Microondas del espectro y opera en banda ISM (Industrial, Scientific and Medical) que va desde 2.4 a 2.4835 GHz.

### Configuración de PC

Se conecta una computadora de escritorio (PC) al router por medio de un cable "copper straight-through" y se utiliza una interfaz de red del tipo FastEthernet que se configura en DHCP para obtener automáticamente una dirección IP.

<img  width="500" src="https://github.com/user-attachments/assets/ef47239a-d594-40ca-9baa-7cda5299e77a" />

<img  width="500" src="https://github.com/user-attachments/assets/72df57bd-f11a-4101-a99a-b73d0a41d6e0" />

### Configuracion de Notebook

Para agregar a la red una notebook primero cambiamos la ranura de expansión que tenia por defecto y le agregamos una NIC Wi-Fi, especificamente la tarjeta inalámbrica WPC300N que permite asociarse al Access Point ya que el módulo soporta protocolos que usa Ethernet para el acceso LAN.

<img  width="500" src="https://github.com/user-attachments/assets/de966853-deeb-4561-b832-51100d397678" />

Luego se procede a conectar la laptop:

<img width="300"  src="https://github.com/user-attachments/assets/ce227e1b-b536-4aca-83a0-2de9a82e38f0" />

<img width="300" src="https://github.com/user-attachments/assets/78a9ee30-b09d-4b8e-b4e6-ca4a57451ef0" />

Con esta nueva conexión ya tenemos nuestra red completa.


<img width="500" src="https://github.com/user-attachments/assets/33a201db-88e2-4e89-9761-1b3b0cd7532a" />

### Conectividad

Como se configuro con DHCP, cada una recibió una IP automática del router:

<img width="500" src="https://github.com/user-attachments/assets/ddf15990-6232-44f4-a968-885ee5649101" />

La PC recibio la IPv4 192.168.0.100 y la laptop recibio la IPv4 192.168.0.101

Por medio del comando ``` ping  [IP del dispositivo destino] ``` se comprueban las conectividades entre los 2 dispositivos individualmente:

Desde la laptop:

<img width="300" src="https://github.com/user-attachments/assets/e6522eea-c91b-4a24-800c-f8b85c70efc9" />

Desde la PC:

<img width="300" src="https://github.com/user-attachments/assets/ea5cb837-04d7-46ee-ad0d-cb5f22bb10e0" />

Interpretaciones de los resultados:

- Ambos equipos tienen conectividad exitosa (0% pérdida) y ell promedio de respuesta (≈27 ms) es similar en ambos casos, lo cual es lógico porque están en la misma red local.

- Los tiempos individuales muestran diferencias: en la PC hay más variabilidad (latencias irregulares) y en la notebook los resultados son más consistentes, lo que indica mayor estabilidad de la conexión inalámbrica en esa simulación. 

En PacketTracer estas diferencias son aleatorias pero se utiliza este ejemplo para analizar un caso posible.

El siguiente comando que se evalua es ``` tracert  [IP del dispositivo destino] ``` el cual sirve para ver el camino que siguen los paquetes desde el dispositivo origen hacia el destino. Envía paquetes ICMP con diferentes valores de TTL (Time To Live), cada router que atraviesa el paquete reduce el TTL en 1 y cuando el TTL llega a 0, ese router responde y se muestra en la salida. Así se va revelando salto por salto toda la ruta.

<img width="500" src="https://github.com/user-attachments/assets/2aaf7733-6856-4cb0-9e46-705aaea5fe10" />

Aqui se puede ver:

a) Columna 1 → Número de salto.

b) Columna 2, 3, 4 → Tiempos de respuesta de cada intento en milisegundos (ms). Se hacen 3 pruebas por salto para ver estabilidad.

c) Columna 5 → Dirección IP o nombre del router/interfaz alcanzada.

En este ejemplo los resultados son mas parejos, por lo que no hay diferencia que cotejar.

---

## Resultados

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se presentan las tablas de IP asignadas, la verificación de conectividad mediante ping y traceroute, y el análisis de cobertura de la red inalámbrica.

## Discusión y conclusiones

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se discuten los resultados obtenidos, las limitaciones del experimento y las posibles mejoras tanto en la configuración de la red como en la metodología de análisis.

---

## Referencias

[1] ...
