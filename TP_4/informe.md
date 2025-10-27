# Trabajo Practico N°4

**Nombres**

- Constanza Medran  
- Fabian N Hidalgo  
- Juan I Vizgarra  
- Sofia V Castro

**Datacenter**

**Universidad Nacional de Córdoba - Facultad de Ciencias Exactas Fisicas y Naturales**  

**Comunicaciones de Datos** 

**Santiago M. Henn - Miguel Solinas** 

**27/10/2025**

---

### Información de los autores

* **Información de contacto**: *victoria.castro@mi.unc.edu.ar - fabian.hidalgo@mi.unc.edu.ar - constanza.medran@mi.unc.edu.ar - juan.vizgarra@mi.unc.edu.ar*

---

## Resumen

En este trabajo se estudian las capas de acceso en redes locales, abordando los estándares y protocolos que permiten la segmentación lógica y el control del tráfico en entornos LAN. 

Se analizan las redes según su alcance, la función de las VLAN (Virtual LAN), y el protocolo IEEE 802.1Q que posibilita la coexistencia de múltiples redes virtuales sobre un mismo enlace físico.

A través de la herramienta Cisco Packet Tracer se implementa una topología de red con switches, router y terminales, aplicando configuraciones de VLANs, NAT y listas de control de acceso (ACLs) para simular diferentes niveles de acceso en una red a bordo de una aeronave. 

Esta práctica permite comprender cómo se gestionan la seguridad, el direccionamiento y la segregación del tráfico en redes modernas.

**Palabras clave:** *VLAN, IEEE 802.1Q, NAT, ACL, redes LAN, virtualización de redes, Packet Tracer*

---

## Introducción

El crecimiento de las redes de datos y la necesidad de gestionar de forma eficiente el tráfico dentro de organizaciones y entornos complejos ha impulsado el desarrollo de mecanismos de segmentación y control a nivel de capa de enlace. En este contexto, las VLAN (Virtual LAN) constituyen una herramienta esencial para dividir lógicamente una red física en múltiples dominios de broadcast, mejorando la seguridad, la eficiencia y la administración de recursos.

El presente trabajo práctico tiene como objetivo poner en práctica los conceptos de capas de acceso, protocolos de enlace y métodos de virtualización de redes locales, implementando una red estructurada en Packet Tracer. A través de la configuración de VLANs, NAT y ACLs, se simulan distintos escenarios de conectividad y acceso, incluyendo el caso particular de una red distribuida en un entorno aeronáutico, donde coexisten distintos perfiles de usuario y requerimientos de servicio.

Esta experiencia permite consolidar conocimientos teóricos de protocolos como IEEE 802.3, IEEE 802.11 y IEEE 802.1Q, comprendiendo cómo interactúan para garantizar la transmisión de datos confiable, segmentada y segura en redes modernas.

---

## Marco Teorico

### Capas de Acceso y Protocolos de Red

En el modelo OSI, la capa de acceso a la red combina las funciones de la capa física y la capa de enlace de datos. Su propósito es establecer, mantener y liberar las conexiones necesarias para la transmisión de datos entre dispositivos dentro de una red local. Esta capa define tanto los medios físicos de conexión (cables, conectores, interfaces) como los protocolos de control de acceso al medio, detección de errores y direccionamiento mediante direcciones MAC.

El estándar IEEE 802.3 (Ethernet) regula la transmisión de datos en redes cableadas mediante el uso de tramas estructuradas y métodos de acceso como CSMA/CD. Por su parte, el IEEE 802.11 define las redes inalámbricas Wi-Fi, que permiten la comunicación por ondas de radio y utilizan mecanismos de control de acceso al medio adaptados a entornos inalámbricos, como CSMA/CA.

### Virtualización de Redes: VLAN y el Protocolo IEEE 802.1Q

Una VLAN (Virtual Local Area Network) permite dividir una red física en múltiples redes lógicas independientes. Cada VLAN constituye un dominio de broadcast separado, lo que reduce el tráfico innecesario y mejora la seguridad y el control de la red.

El protocolo IEEE 802.1Q define el mecanismo de etiquetado o “tagging” de tramas Ethernet, añadiendo un campo de 4 bytes en la cabecera que identifica a qué VLAN pertenece el paquete. Esto posibilita que varias VLAN compartan un mismo enlace físico, especialmente en los enlaces troncales (trunks) entre switches o entre un switch y un router.

Gracias a este protocolo, los dispositivos pueden distinguir qué tráfico pertenece a cada VLAN y reenviarlo adecuadamente, permitiendo la coexistencia de redes lógicas sobre una misma infraestructura física.

### NAT y ACL: Control de Acceso y Traducción de Direcciones

El Network Address Translation (NAT) permite traducir direcciones IP privadas internas a direcciones públicas, habilitando la salida a Internet de múltiples hosts a través de un solo punto de acceso. Existen distintas variantes de NAT (estático, dinámico, PAT), siendo esta última la más común en redes LAN domésticas y empresariales.

Las Access Control Lists (ACLs) son conjuntos de reglas aplicadas a las interfaces de un router o switch que determinan qué tráfico puede pasar o ser bloqueado según criterios como dirección IP, protocolo o puerto. Su combinación con NAT y VLANs permite construir redes jerarquizadas con diferentes niveles de privilegio, tal como se implementa en el escenario práctico del trabajo.

---

## Resultados

### Alcance de Redes y Virtualización

...

### Topologia Packet Tracer

...

### LAN Aeronave

...

---

## Discusión y conclusiones

...

---

## Referencias

[1] - Apuntes de Teoría de las Comunicaciones

[2] - Apuntes de Comunicaciones Digitales

[3] - IEEE 802.3 Ethernet Standard.

[4] - IEEE 802.11 Wi-Fi Standard.

[5] - IEEE 802.1Q VLAN Standard.
