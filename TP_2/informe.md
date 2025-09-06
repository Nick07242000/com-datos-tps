# Título

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

En este trabajo práctico se profundizan conceptos de la capa física y se introduce la capa de enlace de datos en el modelo OSI. 

Se analizan fenómenos de propagación electromagnética que afectan la transmisión de señales y se estudia su impacto en diferentes bandas de frecuencia, relacionando estos efectos con parámetros de calidad como la relación señal-ruido (SNR) y la tasa de error de bit (BER). 

Posteriormente, se utiliza la herramienta Wireshark como analizador de tráfico de red para observar, capturar y estudiar tramas de datos en tiempo real. 

A través de la experimentación con Ethernet y el análisis de direcciones IP y MAC, se investiga la trazabilidad y privacidad de los dispositivos conectados, así como la importancia de estándares y tecnologías como UTP y los distintos tipos de Ethernet.

**Palabras clave:** *capa física, capa de enlace de datos, Ethernet, Wireshark, SNR, BER*

---

## Introducción

El avance de las comunicaciones digitales se sostiene sobre la correcta comprensión de los fenómenos físicos que afectan la propagación de señales y de los mecanismos de control que se aplican en las capas superiores del modelo OSI. En este trabajo práctico se busca consolidar estos conocimientos abordando dos ejes principales: la profundización en los efectos presentes en la capa física y la introducción a la capa de enlace de datos.

En la primera parte se estudian fenómenos que limitan la calidad de transmisión, como la atenuación y el ruido, analizando sus consecuencias sobre distintas bandas de frecuencia y estableciendo vínculos con métricas como SNR y BER. En la segunda parte, se introduce el software Wireshark como herramienta de análisis de tráfico, que permite observar la estructura de las tramas Ethernet, identificar direcciones MAC y fabricantes, y comprender los alcances y limitaciones en términos de privacidad y trazabilidad de dispositivos en la red.

De esta manera, el presente trabajo integra fundamentos teóricos y prácticos, reforzando la relación entre la capa física, la capa de enlace y las herramientas modernas de análisis de redes, con el objetivo de brindar una visión más completa del funcionamiento real de los sistemas de comunicación.

---

# Marco teórico / Modelo / Metodología

## Fenómeno físico – Figura 1

Consignas:
1) Identificar el fenómeno representado y describir sus características principales.
2) Relacionar con las bandas de transmisión (TP1): ¿qué tipos de transmisión son más afectadas y cuáles son más resilientes?
3) Explicar las razones por las que no debe encenderse un celular en un avión y relacionarlo con el fenómeno descrito.

---

## Fenómeno físico – Figura 2

Consignas:
1) Identificar el fenómeno y sus características principales.
2) Relacionar con las bandas de transmisión del TP1.
3) Explicar qué es la SNR, y cómo se relaciona con el BER visto en el TP1.

---

## Análisis con Wireshark

Consignas:

1) Ethernet
Definición y características principales.
Estructura de una trama Ethernet.
Diferencias entre Ethernet, Fast Ethernet y Gigabit Ethernet.

2) Cables UTP
Definición y relación con los fenómenos del ítem 2.
Diferencia entre cable derecho y cable cruzado.

3) Captura de tráfico – Gateway
Determinar la puerta de enlace predeterminada (ipconfig/ifconfig).
Capturar tráfico hacia la gateway con Wireshark.
Documentar el paquete (incluyendo representación en hexadecimal).

4) Dirección MAC
Extraer la dirección MAC del dispositivo.
Consultar el fabricante asociado a la MAC.
Documentar el nombre y dirección de la empresa.

5) Comunicación con otra computadora
Repetir pasos 3 y 4 comunicándose con el dispositivo de un compañero (en la misma red o remotamente).

---

## Resultados

- Presentar los paquetes capturados en Wireshark.
- Incluir extractos en hexadecimal.
- Tablas de direcciones IP y MAC observadas.
- Identificación de fabricantes.
- Análisis de diferencias entre transmisión local y remota.

## Discusión y conclusiones

- Reflexionar sobre la privacidad de un dispositivo en la red.
- Analizar la trazabilidad de una dirección MAC.
- Investigar qué es el IMEI y compararlo con la MAC.
- Responder: ¿Una VPN oculta la dirección MAC del dispositivo?
- Conectar con los resultados obtenidos en el laboratorio y las capturas de Wireshark.

---

## Referencias

[1] - Apuntes de Teoría de las Comunicaciones

[2] - Apuntes de Comunicaciones Digitales

[3] - IEEE 802.3 Ethernet Standard.

[4] - Wireshark Foundation. Wireshark User Guide