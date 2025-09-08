# Trabajo Practico N°2

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

## Marco Teorico

La capa física constituye el nivel más bajo del modelo OSI y se encarga de la transmisión real de bits a través del medio de comunicación, definiendo aspectos como voltajes, frecuencias, modulaciones, conectores y medios físicos (cobre, fibra óptica, radiofrecuencia). Sobre ella se apoya la capa de enlace de datos, cuyo rol es garantizar la entrega confiable de tramas entre nodos directamente conectados, gestionando direcciones físicas (MAC), detección de errores y control de acceso al medio, a través de protocolos como Ethernet o Wi-Fi. Para el estudio y análisis de estas capas resulta fundamental el uso de herramientas de captura de tráfico como Wireshark, un analizador de protocolos que permite observar en tiempo real los paquetes que circulan por una red, inspeccionar su estructura en distintos niveles del modelo OSI, y relacionar fenómenos de la capa física con su representación en tramas de la capa de enlace, constituyendo un recurso esencial para la comprensión y el diagnóstico de sistemas de comunicación digital.

---

## Resultados

### Fenómeno físico – Figura 1

<p align="center">
  <img width="700" height="300" alt="image" src="https://github.com/user-attachments/assets/ffd7624b-6aec-4ccf-a523-ca83a886e8bc">
</p>

a) El fenómeno físico representado por la señal transmitida desde el barco hacia el satélite es el efecto Doppler ya que el barco se va moviendo mientras sigue enviando la señal. Su posición respecto al satélite está cambiando continuamente. Esto produce que a medida que se acerque al satélite su frecuencia aumenta y disminuye la longitud de onda, mientras que cuando se aleja ocurre a la inversa: disminuye la frecuencia y aumenta la longitud de onda.

b) Este fenómeno influye en todas las ondas electromagnéticas pero afecta más a las señales de alta frecuencia (ej: microondas) ya que su ecuación así lo dictamina: a mayor frecuencia portadora, mayor desplazamiento absoluto en Hz. Se puede ver con mayor claridad por ejemplo a señales de GPS, satelitales, etc que se encuentran en la parte de microondas del espectro. En las ondas de baja frecuencia (como ondas de radio) el efecto no es tan marcado si se compara con la frecuencia de la portadora.

c) No se debe encender el celular en un avión principalmente para evitar interferencias electromagnéticas en los sistemas de comunicación y navegación del avión ya que los celulares emiten radiofrecuencia en bandas como GSM, 3G, 4G o 5G. Las señales de RF pueden inducir ruidos en equipos electrónicos sensibles de la aeronave, como: sistemas de navegación (ej: GPS), comunicaciones avión-torre o sensores de vuelo. 
Sí hay una conexión indirecta: el teléfono y las torres se mueven rápidamente uno respecto al otro, generando desplazamiento Doppler de la señal.
A frecuencias bajas (GSM ~900 MHz) el Doppler es pequeño, pero en vuelos comerciales (~900 km/h) puede afectar la sincronización de la señal y causar errores en la comunicación. 
En resumen, considerando la velocidad del avión, la frecuencia de la señal de un celular puede desplazarse lo suficiente para complicar la recepción en las estaciones base terrestres. 

---

### Fenómeno físico – Figura 2

<p align="center">
  <img src="https://github.com/user-attachments/assets/93089115-30bd-4444-a79b-6ba4d1038f4c" alt="Onda" width="700" height="300">
</p>

a) En la imagen se puede observar la representacion del ruido en la señal de comunicacion. Este es un fenómeno físico inevitable que ocurre cuando una señal no deseada se añade a la señal de información, distorsionándola.

El ruido posee las siguientes caracteristicas:
- Aleatorio: El ruido es una señal impredecible que carece de una forma de onda o patrón definido.
- Indeseable: A diferencia de la señal portadora, el ruido no transmite información útil y, en cambio, degrada la calidad de la señal original.
- Aditivo: El ruido se superpone a la señal útil durante la transmisión. La señal que llega al receptor es una suma de la señal original y la señal de ruido. En el gráfico, esto se visualiza como una onda distorsionada en el punto donde se encuentra la fuente de ruido (el trabajador con el martillo percutor).

b) La transmision de señales inalambricas es la mas afectada, principalmente por contaminacion del medio lo que puede generar que se mezclen con otras fuentes de ruido y señales de radio distorsionando la señal. 

Entre las posibles fuentes de ruido tenemos:
- Ondas Electromagneticas: Ruido generado por motores electricos, electrodomesticos (microondas) y emisoras de radio frecuencias.
- Interferencia de señal adyacente: Varias redes inalambricas operando en el mismo espectro de frecuencia pueden interferir entre si.

La fibra optica es la mas resiliente al ruido. A diferencia de las señales electricas o de radio estas viajan por medio de emisiones de luz.
- Inmunidad a la EMI: Al usar luz, las señales de fibra óptica son completamente inmunes a las interferencias electromagnéticas, que son la causa principal de ruido en los medios de cobre y aire.
- Atenuación mínima: Aunque las señales de luz también experimentan una mínima atenuación por impurezas en el vidrio, esta pérdida es significativamente menor que la que ocurre en otros medios, lo que permite la transmisión de datos a velocidades y distancias mucho mayores sin necesidad de repetidores.

Las transmisiones por cable coaxial son un punto intermedio. Son más resilientes que las inalámbricas porque el cable está físicamente blindado, lo que ayuda a proteger la señal de la EMI externa. Sin embargo, siguen siendo susceptibles al ruido si el blindaje está dañado o si la longitud del cable es excesiva, causando pérdidas de señal.

c) La Relación Señal-Ruido (SNR) es una medida que compara la potencia de una señal deseada (información) con la potencia del ruido no deseado que la acompaña. Se expresa en decibelios (dB) y es un indicador clave de la calidad de la señal.
  -SNR alta: Significa que la señal es mucho más potente que el ruido, lo que resulta en una transmisión más clara y confiable.
  -SNR baja: Indica que el ruido tiene una potencia comparable a la de la señal, lo que la degrada y dificulta su correcta decodificación.
  
La Tasa de Error de Bits (BER) es la proporción de bits que se han recibido con errores en una transmisión digital, en comparación con el número total de bits transmitidos. Por ejemplo, una BER de 10⁻³ significa que, en promedio, un bit de cada 1000 llega con error. Este concepto fue mencionado en el TP1.

La SNR y la BER están directamente relacionadas. La SNR (Relación Señal-Ruido) es un concepto fundamental que explica la calidad de una señal en relación con el ruido, mientras que la BER (Tasa de Error de Bits) es una métrica que mide la consecuencia de una SNR baja en sistemas digitales.

Si la señal es mucho más fuerte que el ruido (SNR alta), es muy probable que los bits se reciban correctamente, resultando en una baja tasa de errores. Por el contrario, si la señal está contaminada por un ruido fuerte (SNR baja), el receptor tendrá dificultades para diferenciar los bits "1" de los bits "0", lo que aumentará la tasa de errores. Entonces podemos decir que a mayor SNR, menor será la BER.

---

### Análisis con Wireshark

a) Ethernet es una familia de tecnologías de red de área local (LAN) definidas en el estándar IEEE 802.3. Proporciona un método de acceso al medio basado en transmisión por paquetes y constituye actualmente la tecnología de red cableada más utilizada a nivel mundial.

Sus características principales son:
- Topología física: originalmente en bus, actualmente en estrella conmutada mediante switches.
- Método de acceso al medio: usa CSMA/CD (Carrier Sense Multiple Access with Collision Detection) en sus versiones originales sobre medios compartidos; en redes modernas con switches dedicados, este método ha quedado prácticamente obsoleto al eliminarse las colisiones.
- Direccionamiento: cada dispositivo tiene una dirección física única de 48 bits conocida como MAC (Media Access Control).
- Unidad de transmisión: trabaja con tramas de datos que encapsulan la información proveniente de capas superiores.
- Velocidades soportadas: desde 10 Mbps hasta decenas de Gbps en versiones modernas.
- Medios físicos: pares trenzados, coaxial en versiones antiguas, y fibra óptica en implementaciones de alta velocidad.

Una trama Ethernet típica se compone de los siguientes campos:
- Preamble: es la secuencia para la sincronizacion del receptor.
- Start Frame Delimiter: indica el inicio de la trama.
- MAC destino: direccion fisica del receptor.
- MAC origen: direccion fisica del emisor.
- Tipo/Longitud: identifica el protocolo de la capa superior.
- Datos: la informacion transmitida
- Frame Check Sequence: codigo CRC para deteccion de errores

Podemos distinguir las siguientes iteraciones de Ethernet:
- Ethernet (10 Mbps): Primera versión estandarizada, operaba sobre coaxial y posteriormente sobre par trenzado. Baja velocidad para estándares actuales.
- Fast Ethernet (100 Mbps): Introduce mayor velocidad manteniendo compatibilidad con Ethernet clásico. Usa par trenzado o fibra.
- Gigabit Ethernet (1000 Mbps): Multiplica por 10 la velocidad de Fast Ethernet, permitiendo transmisión a 1 Gbps sobre cobre y fibra óptica. Mantiene compatibilidad con estándares anteriores y se convierte en el estándar de facto en redes LAN modernas.

Al hablar de diferencias entre estas la velocidad de transmisión es la principal distinción. Ademas, los requisitos del medio físico son más exigentes en cada evolución pero se mantiene el formato de trama y los principios de direccionamiento, asegurando interoperabilidad entre generaciones.

b) Un cable UTP (Unshielded Twisted Pair) es un medio de transmisión compuesto por pares de conductores de cobre trenzados entre sí, sin apantallamiento externo. Es el tipo de cable más utilizado en redes Ethernet modernas debido a su bajo costo, facilidad de instalación y buen rendimiento en distancias típicas de LAN (hasta 100 metros en la mayoría de sus categorías).

La técnica de trenzado de los pares de conductores tiene como objetivo reducir la interferencia electromagnética (EMI) y el crosstalk (acoplamiento de señal entre pares adyacentes), donde cada par transporta una señal diferencial (la información se codifica en la diferencia de potencial entre los dos conductores).

De esta forma, el trenzado alterna la posición de los conductores, haciendo que las interferencias externas afecten de forma similar a ambos hilos; como consecuencia, al restar las señales, el ruido común se cancela, por lo que el diseño del cable busca mejorar la SNR y asi reducir el BER en la transmision.

Un cable de UTP derecho conecta cada pin de un extremo al mismo pin del otro, se utiliza para conectar dispositivos diferentes, mientras que un UTP cruzado intercambia las líneas de transmisión con las de recepción y se utiliza para conectar dispositivos similares sin necesidad de un hub o switch intermedio.

c) Para capturar un paquete con Wireshark, comenzamos realizando ipconfig para obtener la puerta de enlace predeterminada:

<img width="545" height="329" alt="image" src="https://github.com/user-attachments/assets/20324e87-93c4-45ca-a223-61f384db936f" />

Con esto ejecutamos un ping hacia la puerta de enlace:

<img width="454" height="200" alt="image" src="https://github.com/user-attachments/assets/f57df022-2356-44d9-86fb-acb0df8dafbb" />

Y capturamos el siguiente paquete:

<img width="1027" height="38" alt="image" src="https://github.com/user-attachments/assets/cfe9b6f6-7640-4c52-98a9-02276a835311" />

<img width="994" height="63" alt="image" src="https://github.com/user-attachments/assets/03a7eabd-70bb-4adf-96ac-f7d5555d6f77" />

<img width="535" height="84" alt="image" src="https://github.com/user-attachments/assets/a7b1b8ff-809e-4a08-b5c2-8124df118c39" />

d) Para obtener la direccion MAC, nos fijamos en los primeros 6 bytes del paquete, donde se encuentra la direccion MAC del destino:

<img width="774" height="77" alt="image" src="https://github.com/user-attachments/assets/99e81af1-df12-43f2-aad1-a3966d7ef5ff" />

Esta es a8:6a:bb:dd:2a:32. Luego con esto investigamos informacion sobre el fabricante:

<img width="1162" height="509" alt="image" src="https://github.com/user-attachments/assets/8b92d3cc-eba6-403b-b825-b7cb5068e79c" />

e) Para comunicarnos con otra computadora, obtenemos la direccion ip local de la computadora con la que queres comunicarnos (al estar en la misma red), y enviamos un ping.

<img width="455" height="200" alt="image" src="https://github.com/user-attachments/assets/35dca831-b5c2-4250-8ab0-6e4f631a2a9a" />

En Wireshark capturamos un paquete:

<img width="1031" height="42" alt="image" src="https://github.com/user-attachments/assets/ea8053e3-bb23-4671-b7f8-c912fbeb1022" />

<img width="991" height="61" alt="image" src="https://github.com/user-attachments/assets/eb24ff9a-04ac-49a4-9c3c-f5f4cfc15167" />

<img width="531" height="85" alt="image" src="https://github.com/user-attachments/assets/2a33fe27-7eb6-4386-92fa-0d1663880157" />

Y obtenemos la informacion sobre el fabricante:

<img width="1164" height="511" alt="image" src="https://github.com/user-attachments/assets/eadd9762-8d81-4a9f-9521-624075673423" />

---

## Discusión y conclusiones

Respecto a la privacidad de un dispositivo en la red, a través de Wireshark, observamos cómo las tramas Ethernet exponen información sensible, como direcciones MAC únicas que identifican hardware específico. Esto implica que, en una red local, cualquier entidad con acceso al tráfico (por ejemplo, un administrador de red o un atacante) puede monitorear y rastrear dispositivos sin el consentimiento del usuario. En el contexto de redes públicas, como Wi-Fi abiertas, esta exposición aumenta el riesgo de violaciones de privacidad, ya que herramientas como Wireshark permiten capturar y analizar paquetes en tiempo real. Sin embargo, medidas como el uso de encriptación (por ejemplo, WPA3 en Wi-Fi) o el spoofing de MAC (cambiar temporalmente la dirección) pueden mitigar estos riesgos, aunque no eliminan por completo la vulnerabilidad inherente a la capa de enlace. Las pruebas que realizamos, como el ping a la puerta de enlace y a otro dispositivo, demuestran cómo datos aparentemente inofensivos (como MAC de un router o una PC) pueden revelar detalles sobre el entorno del usuario, subrayando la necesidad de conciencia sobre la exposición de datos en redes.

En cuanto a la trazabilidad de una dirección MAC, esta actúa como un identificador único asignado por el fabricante a la interfaz de red de un dispositivo, compuesto por 48 bits (por ejemplo, a8:6a:bb:dd:2a:32 en nuestras capturas). En redes locales, la MAC permite rastrear el movimiento y la actividad de un dispositivo, ya que se incluye en cada trama Ethernet. Esto facilita la trazabilidad en entornos controlados, como redes empresariales, donde se puede mapear dispositivos para gestión de seguridad. Sin embargo, su trazabilidad es limitada a nivel global: la MAC no se propaga más allá de la red local (no viaja en paquetes IP a través de internet), lo que la hace menos útil para seguimiento remoto comparado con una IP. 

El IMEI (International Mobile Equipment Identity) es un número que se le asigna a cada dispositivo móvil que lo identifica de forma global en redes de telecomunicaciones. Si bien IMEI y MAC son ambos identificadores únicos que permiten rastrear los dispositivos, la diferencia está en su ámbito de aplicación: el IMEI es para redes móviles y la MAC para redes locales. Además, el IMEI es de mayor alcance, ya que es global, mientras que las MAC son locales, dentro de la red a la que está conectado el dispositivo.

Una VPN (Virtual Private Network) no oculta la dirección MAC del dispositivo. Lo que hace es enmascarar la dirección IP pública del dispositivo para ocultarla, redirigiendo el tráfico a través de un servidor VPN remoto, protegiendo la privacidad del dispositivo frente a servidores externos en internet, ya que no pueden ver la IP original ni rastrear su ubicación real. Sin embargo el VPN funciona en la capa de red y la dirección MAC es un identificador de la capa de enlace de datos, utilizado para la comunicación entre dispositivos en la misma red local. Al no intervenir en la misma capa, la dirección MAC sigue siendo visible dentro de la red local a la que está conectada por cualquier otro dispositivo o router, aunque se esté utilizando una VPN. 

En conclusión, en este trabajo práctico hemos profundizado en conceptos fundamentales como el efecto Doppler, las interferencias en señales, la tecnología Ethernet y los identificadores únicos como las direcciones MAC y el IMEI. Es importante destacar que todos estos elementos convergen en la esencia de las comunicaciones y la gestión de dispositivos. El efecto Doppler modula frecuencias, las interferencias afectan amplitudes, y Ethernet conecta redes, nuestras direcciones MAC e IMEI nos identifican en ese entorno interconectado digital. 
En particular, las VPN ofrecen una capa de protección al encriptar el tráfico y ocultar la IP pública, pero no afectan la visibilidad de la MAC en redes locales, lo que resalta limitaciones en la privacidad absoluta. Aunque una VPN puede proporcionar protección en la capa de red, la dirección MAC sigue siendo un punto débil en la capa de enlace de datos dentro de una red local. La comprensión de estas diferencias y la implementación de medidas adicionales de privacidad son esenciales para una seguridad integral, mejorando la experiencia del usuario y el funcionamiento de las aplicaciones y servicios que dependen de ellas.
En resumen, estos conceptos forman el tejido invisible que sostiene nuestra conectividad y seguridad en el mundo digital.

---

## Referencias

[1] - Apuntes de Teoría de las Comunicaciones

[2] - Apuntes de Comunicaciones Digitales

[3] - IEEE 802.3 Ethernet Standard.

[4] - Wireshark Foundation. Wireshark User Guide
