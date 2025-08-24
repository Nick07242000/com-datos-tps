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

Los parámetros básicos configurados fueron:

* Dirección IP del router: 192.168.0.1
* Máscara de subred: 255.255.255.0
* SSID: ...
* Seguridad: WPA2-PSK

_router: en q frecuencia opera + q region del espectro corresponde + en q banda opera_

### Configuración de PC

_q hicimos_

### Configuracion de Notebook

_q hicimos_

### Conectividad

_resultados_

__

---

## Resultados

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se presentan las tablas de IP asignadas, la verificación de conectividad mediante ping y traceroute, y el análisis de cobertura de la red inalámbrica.

## Discusión y conclusiones

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Se discuten los resultados obtenidos, las limitaciones del experimento y las posibles mejoras tanto en la configuración de la red como en la metodología de análisis.

---

## Referencias

[1] ...
