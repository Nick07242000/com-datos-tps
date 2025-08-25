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

* **Ondas electromagnéticas**: Perturbación que se propaga a través del espacio, compuestas por campos eléctricos y magnéticos que oscilan de manera perpendicular entre sí.  
* **Modulación y demodulación**: Proceso de modificar una señal portadora (generalmente de alta frecuencia) con la información de una señal de mensaje para que esta última pueda ser transmitida de manera eficiente a larga distancia. En el otro extremo, la demodulación es el proceso inverso, donde se recupera la señal de mensaje original a partir de la señal portadora modulada.  
* **Señales en tiempo continuo**: Tambien llamada *señal analógica*, es aquella que se define para cada instante de tiempo. Es decir, su amplitud puede tomar cualquier valor dentro de un rango continuo.  
* **Señales en tiempo discreto**: O *señal digital*, solo se define en instantes de tiempo específicos y discretos. Estas señales se obtienen al muestrear una señal de tiempo continuo a intervalos regulares, por lo que su amplitud solo puede tomar un conjunto finito de valores.

### Análisis de Fenómenos y Espectro Electromagnético

Dada la siguiente onda electromagnética:

*imagen del grafico \- se inserta en Github*

*Luego de analizar el grafico podemos sacar como dato la longitud de la onda, sabiendo la constante de la velocidad de propagacion de la luz, realizamos la siguiente formula:*

v \=λf  

    λ \= 60 \[mm\]	              v \= 3x108\[m/s\]

          f \= v/f \= 5x109\[Hz\]  \= 5 GHz

| Parámetro | Valor estimado | Unidad |
| :---- | :---- | :---- |
| Frecuencia | 5 | GHz |
| Longitud de onda | 60 | mm |

c)- La onda opera en la región de las **microondas**. Según las definiciones de la Unión Internacional de Telecomunicaciones (ITU),a una frecuencia de 5 GHz se encuentra en la **banda C** o **Banda SHF** (Super High Frequency).

Segun la ITU:

* **Banda SHF:** Esta región del espectro electromagnético abarca frecuencias de **3 GHz a 30 GHz**. La frecuencia de 5 GHz cae directamente en este rango.  
* **Banda C:** Esta banda, definida para ciertas aplicaciones, generalmente abarca un rango de frecuencias que incluye 5 GHz. Por ejemplo, en telecomunicaciones satelitales, la banda C se utiliza para la transmisión de señales en este rango de frecuencia.

d)- Existen varios dispositivos de comunicación de datos operan en el rango de \[3-30\]GHz de frecuencia.

* **Puntos de acceso Wi-Fi y routers inalámbricos:** Muchos dispositivos de redes Wi-Fi modernas, especialmente los que utilizan los estándares 802.11n, 802.11ac y 802.11ax (Wi-Fi 4, 5 y 6), operan en la banda de 5 GHz. Esto permite una mayor velocidad de datos y menos interferencia que la banda de 2.4 GHz.  
* **Comunicaciones por satélite:** La banda C es ampliamente utilizada en la comunicación satelital para transmisiones de televisión y telefonía.  
* **Redes de área metropolitana inalámbricas (WMAN):** Tecnologías como WiMAX a menudo usan la banda de 5 GHz para proporcionar conectividad de banda ancha a grandes áreas.

Un ejemplo de un dispositivo que opera en esta banda es el **router inalámbrico WRT300N,** tipo de router que es compatible con el estándar 802.11n, que utiliza tanto las bandas de 2.4 GHz como 5 GHz para la transmisión de datos.

e)- Con la linea roja situada en el grafico podemos observar el fenomeno de la atenuacion, que es la perdida de intensidad o potencia de la señal en un medio de transmision, a medida que se desplaza la onda. Esta puede ser causada por resistencia y absorcion, longitud del cable en la que se transporta, interferencias , entre otras.

En alta frecuencia el vapor de agua junto con otros gases son capaces de absorber la energia de la señal.

f)- El router inalambrico se ve significativamente afectado. En la vida cotidiana la atenuacion provoca que la conexion WiFi domestica, a medida que te alejas del router, la señal disminuye junto con la velocidad y suele llegar a perder la señal con la suficiente distancia. Tambien la afectan objetos tales como las paredes, muebles y personas.

g) **Telefonía celular:** Son afectadas las ondas de radio al perder fuerza a medida que se alejan de la antena, lo que provoca una señal más débil en distancias largas o en zonas con obstáculos (como paredes gruesas).

**Cable coaxial:** Si son afectadas ya que la señal eléctrica se debilita a medida que recorre el cable debido a la resistencia y otras pérdidas. Esta pérdida es mayor en cables más largos y a frecuencias más altas.

**Fibra óptica:** La atenuación se produce por la absorción y dispersión de la luz dentro del cable de fibra. Sin embargo, es un fenómeno mucho menos significativo que en los medios eléctricos, lo que permite la transmisión de datos a muy largas distancias.
Es decir que son afectadas pero en menor medida en comparacion a los medios anteriores.

---

## Análisis de Sistemas Digitales

Comunicar datos a través de cualquier medio es, en esencia, un proceso que consiste en modificar el comportamiento de una señal en el tiempo.

En esta materia nos concentramos en la transmisión de datos, hoy por hoy, dominado por las señales digitales.

El siguiente sistema:

<img width="618" height="185" alt="image" src="https://github.com/user-attachments/assets/75dcb841-6dc4-4344-9c56-ce6c460d9874" />

Corresponde a un modo de transmisión síncrono y paralelo simple en cuanto al canal (datos + reloj), donde la comunicación es unidireccional (del emisor hacia el receptor), y la sincronización está garantizada mediante la línea de reloj transmitida junto con la señal de datos.

Según su direccionalidad y características temporales, decimos que es simplex ya que la comunicacion ocurre en un solo sentido, y de transmision en derie ya que los datos se envian de forma secuencial por un mismo canal.

Este paradigma no es el mas adecuado si quisieramos transmitir datos rapidamente y de forma direccional, ya que para la bidireccionalidad deberian duplicarse las lineas de comunicacion, siendo asi una comunicacion full-duplex. 

Ademas, en cuanto a la velocidad de la transmision, el desfase entre la línea de datos y la línea de reloj hace que el sistema pierda sincronización conforme aumenta la tasa de bits.

### Representación UART y codificación de caracteres

Teniendo en cuenta que en la expresión más simple de señal digital, podemos pensar que un nivel de tensión “1” representa un 1 digital, y un nivel de tensión “0” representa un 0 digital.

Si quisieramos transmitir la cuarta letra del nombre del grupo 'a' en codificacion ASCII (01000001), la señal se veria de la forma:

<img width="609" height="167" alt="image" src="https://github.com/user-attachments/assets/dd43c373-a2fa-4cf5-93d5-ad65b18b633d" />

Teniendo en cuenta los niveles de tension al pasar de 0 a 1 o viceversa, para evitar la zona de transición (pendiente), la decisión del bit debe hacerse en el instante medio de cada período de bit, no sobre los flancos. Esto puede visualizarse en el siguiente grafico:

<img width="647" height="239" alt="image" src="https://github.com/user-attachments/assets/69dfb24d-4594-4b91-931f-0cac3435a433" />

---

## Limitaciones de Transmisión Inalámbrica de Señales Escalonadas

Transmitir señales escalonadas (o pulsos cuadrados) de forma inalámbrica presenta varios inconvenientes derivados de su análisis espectral y las limitaciones del medio de transmisión. Según la transformada de Fourier, una señal cuadrada ideal requiere un ancho de banda infinito, ya que se compone de una fundamental más armónicos infinitos de frecuencias cada vez más altas. Esto genera varios inconvenientes:

- **Ineficiencia espectral**: ocuparía un ancho de banda enorme, interfiriendo con otros sistemas inalámbricos.  
- **Atenuación de altas frecuencias**: las componentes de alta frecuencia se degradan rápidamente en medios reales, reduciendo la fidelidad de la señal recibida.  
- **Sensibilidad al ruido**: al tener tantas componentes espectrales, cualquier interferencia externa puede distorsionar gravemente la señal.  
- **Alto consumo de potencia**: generar y transmitir pulsos tan “agudos” demanda más energía y hardware complejo.  

Por estos motivos, la transmisión inalámbrica moderna no envía directamente señales digitales escalonadas, sino que se **modulan sobre ondas sinusoidales** (portadoras analógicas) que viajan de forma más estable y eficiente.

---

## Análisis del gráfico

### a) Técnica de modulación representada
El gráfico muestra un ejemplo de **ASK (Amplitude Shift Keying)**.  
En esta técnica, la amplitud de la portadora varía según el bit transmitido:  
- Bit **1** → portadora con amplitud máxima.  
- Bit **0** → portadora con amplitud reducida o nula.

La ASK es una forma sencilla de modulación en la que se manipula la amplitud de la
 portadora para transmitir la información digital. Este tipo de modulación es útil en
 comunicaciones donde se necesita una implementación simple, aunque puede ser más
 susceptible al ruido y las interferencias en comparación con otras técnicas de modulación
 como FSK o PSK.

### b) Ejemplo de señal digital modulada
<img width="786" height="191" alt="image" src="https://github.com/user-attachments/assets/f47a475e-6eb8-47f6-bee6-fb68c8b1bae9" />


### c) Otras técnicas de modulación relacionadas
Existen tambien otras técnicas basadas en modificar parámetros de una portadora sinusoidal (amplitud, frecuencia o fase) para transmitir datos digitales

- **Modulación por Desplazamiento de Frecuencia (FSK):**  
  La frecuencia de la onda portadora se varía en función de los datos digitales. Por ejemplo, se puede utilizar una frecuencia para representar un bit **"0"** y otra frecuencia para representar un bit **"1"**.

- **Modulación por Desplazamiento de Fase (PSK):**  
  En PSK, la fase de la onda portadora se cambia para representar los datos.  
  - En **BPSK (Binary Phase Shift Keying)**, se utilizan dos fases (0° y 180°) para representar los bits "0" y "1".  
  - En **QPSK (Quadrature Phase Shift Keying)**, se utilizan cuatro fases para representar **2 bits por símbolo**.

- **Modulación por Amplitud en Cuadratura (QAM):**  
  Esta técnica combina ASK y PSK. Tanto la amplitud como la fase de la portadora se modifican para representar los datos. Por ejemplo, **16-QAM** puede representar **4 bits por símbolo** al utilizar 16 combinaciones diferentes de amplitud y fase.

- **Modulación por Pulsos (PAM – Pulse Amplitude Modulation):**  
  Similar a ASK, en PAM se varía la amplitud de los pulsos en función de la señal de entrada. Esta técnica se utiliza a menudo en sistemas de transmisión digital.

- **Modulación por Desplazamiento de Frecuencia en Cuadratura (QFSK):**  
  Es una variante de FSK que utiliza dos frecuencias para representar dos bits, similar a cómo QPSK utiliza dos bits por fase.


### d) Bit Error Rate (BER)
El Bit Error Rate (BER) es una métrica de rendimiento que mide la proporción de bits recibidos erróneamente respecto al total transmitidos en un canal. Depende de factores como ruido, interferencia y SNR. Un BER bajo (ej. 10^{-5}) indica mayor fiabilidad.

En términos de BER, entre las técnicas mencionadas, PSK (especialmente BPSK y QPSK) ofrece las mejores prestaciones, ya que es más robusta al ruido de amplitud al depender solo de la fase. FSK es intermedia, resistente a variaciones de amplitud pero sensible a interferencias frecuenciales. ASK tiene el peor rendimiento, ya que el ruido afecta directamente la amplitud, aumentando los errores en canales ruidosos. Técnicas avanzadas como QAM pueden tener BER más alto en condiciones adversas, pero optimizan otros aspectos como eficiencia espectral.


## Implementación en Packet Tracer

Se implementó una red simple compuesta por un router inalámbrico, una computadora de escritorio conectada mediante cable y una notebook conectada vía Wi-Fi.

### Configuración de Router

<img  width="500" src="https://github.com/user-attachments/assets/bc0b0dd3-f1a3-4f79-baed-26e70b65b0f7" /><br>

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

<img  width="500" src="https://github.com/user-attachments/assets/ef47239a-d594-40ca-9baa-7cda5299e77a" /><br>

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

### Conexión de nueva laptop

Se agrega en la vista física una nueva conexión (laptop1) con la que verificaremos el alcance y la conexión de la red Wi-Fi al conectarse con otro dispositivo dentro de la red que tengan una conexión al 100%.

Primero se coloca la computadora en una posición donde la señal llega al 4%: 

<img width="300" src="https://github.com/user-attachments/assets/fb1ad25d-d7bc-4ece-a4b6-f6fa6bad0027" /><br>

<img width="400" src="https://github.com/user-attachments/assets/9d2df8b0-7404-49c9-81ff-b22ecdefe992" />

Luego se intenta contar con alguna de las máquinas conectadas al 100% y se obtiene:

<img width="500" src="https://github.com/user-attachments/assets/16222374-70e2-4ae1-b13a-034e359209bc" />

Podemos ver que obtenemos mejores tiempos de transmisión de datos de lo que se podría haber esperado al estar tan lejos de la señal del router.

Para el siguiente caso, se la aleja aún más de la señal.

<img width="400" src="https://github.com/user-attachments/assets/26c5be28-b743-4545-87ec-85ada2beaa9a" />

Ya al no tener señal del router (0%), no puede transferir datos a otros dispositivos de la red. Prueba 4 veces sin resultados positivos.

<img width="500" src="https://github.com/user-attachments/assets/63834917-0610-4810-903c-7c74f7d24602" />

---

## Resultados

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se presentan las tablas de IP asignadas, la verificación de conectividad mediante ping y traceroute, y el análisis de cobertura de la red inalámbrica.

## Discusión y conclusiones

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se discuten los resultados obtenidos, las limitaciones del experimento y las posibles mejoras tanto en la configuración de la red como en la metodología de análisis.

---

## Referencias

[1] ...
