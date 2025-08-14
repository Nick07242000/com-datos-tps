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