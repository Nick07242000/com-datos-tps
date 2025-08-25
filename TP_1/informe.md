# Título

**Nombres**

- Constanza Medran  
- Fabian N Hidalgo  
- Juan I Vizgarra  
- Sofia V Castro

**Datacenter**

**Universidad Nacional de Córdoba \- Facultad de Ciencias Exactas Fisicas y Naturales**  
**Comunicaciones de Datos** **TBD** **TBD**

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

En el siguiente sistema:

*imagen del sistema \- Github insert*

*explicacion de tipo y modo de transmision*

*justificacion del paradigma (sea o no el mejor)*

### Representación UART y codificación de caracteres

Teniendo en cuenta que en la expresión más simple de señal digital, podemos pensar que un nivel de tensión “1” representa un 1 digital, y un nivel de tensión “0” representa un 0 digital.

Si quisieramos transmitir la cuarta letra del nombre del grupo 'a' en codificacion ASCII, la señal se veria de la forma:

*grafico UART*

Teniendo en cuenta los niveles de tension al pasar de 0 a 1 o viceversa *En qué marcas temporales medirían la señal para determinar el valor digital de la misma*

---

## Limitaciones de Transmisión Inalámbrica de Señales Escalonadas

*Investigar y resumir brevemente los motivos por los cuales no es conveniente transmitir de manera inalámbrica una señal escalonada*

Es por esto que existen otras tecnicas de modulacion como: *la tecnica del grafico*

*paint de como ser veria la señal digital modulada*

*otras técnicas de modulación basadas en los mismos principios*

Un termino importante en la modulacion de señales es BER *definicion \+ cual tecnica es mejor*

---

## Implementación en Packet Tracer

Se implementó una red simple compuesta por un router inalámbrico, una computadora de escritorio conectada mediante cable y una notebook conectada vía Wi-Fi.

### Configuración de Router

Los parámetros básicos configurados fueron:

* Dirección IP del router: 192.168.0.1  
* Máscara de subred: 255.255.255.0  
* SSID: ...  
* Seguridad: WPA2-PSK

*router: en q frecuencia opera \+ q region del espectro corresponde \+ en q banda opera*

### Configuración de PC

*q hicimos*

### Configuracion de Notebook

*q hicimos*

### Conectividad

*resultados*

\_\_

---

## Resultados

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se presentan las tablas de IP asignadas, la verificación de conectividad mediante ping y traceroute, y el análisis de cobertura de la red inalámbrica.

## Discusión y conclusiones

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se discuten los resultados obtenidos, las limitaciones del experimento y las posibles mejoras tanto en la configuración de la red como en la metodología de análisis.

---

## Referencias

\[1\] ...  
