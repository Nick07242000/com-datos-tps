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

Simulamos el despliegue de una red LAN a bordo de una aeronave, con la siguiente configuracion:
- Clase Turista --> acceso a solo un sistema de entretenimiento (server local)
- Clase Business --> acceso a sistema de entretenimiento e internet
- Administracion --> acceso a total

<img width="730" height="243" alt="image" src="https://github.com/user-attachments/assets/2af97473-0ada-4c41-b906-4b1423a9901a" />

Para esto usamos la siguiente topologia:

Diagrama | Implementacion
:------------------------:|:-------------------------:
<img width="533" height="462" alt="image" src="https://github.com/user-attachments/assets/d19e2c57-29cc-4f6d-b6d0-1a8566eb07cd" /> | <img width="588" height="440" alt="image" src="https://github.com/user-attachments/assets/3682c853-2ccd-4bac-a07b-8d45a5eb53e6" />

Y la siguiente tabla de direccionamiento:

VLAN | Nombre | Red IP | Gateway | Acceso
:--------:|:--------:|:--------:|:--------:|:--------:
10 | Turista | 10.10.10.0/24 | 10.10.10.1 | Solo server
20 | Business | 10.10.20.0/24 | 10.10.20.1 | Server + Internet
99 | Administracion | 10.10.99.0/24 | 10.10.99.1 | Acceso total
-- | Enlace ISP | 200.0.0.0/30 | 200.0.0.1-2 | --

#### Configuracion ISP

Configuramos el router del ISP para habilitar el puerto FastEthernet0/0 para conectar con el router del avion:

```text
Router>enable
Router#config t
Router(config)#interface FastEthernet0/0
Router(config-if)#no shutdown
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up
```

#### Configuracion Router Avion

Configuramos el puerto FastEthernet0/0 para conectar con el switch del avion:

```text
Router>enable
Router#config t
Router(config)#interface FastEthernet0/0
Router(config-if)#no shutdown
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up
```

Configuramos las subinterfaces para gestionar las VLANs en el puerto FE0/0:

```text
Router(config)#interface FastEthernet0/0.10
%LINK-5-CHANGED: Interface FastEthernet0/0.10, changed state to up
Router(config-subif)#encapsulation dot1Q 10
Router(config-subif)#ip address 10.10.10.1 255.255.255.0

Router(config)#interface FastEthernet0/0.20
%LINK-5-CHANGED: Interface FastEthernet0/0.20, changed state to up
Router(config-subif)#encapsulation dot1Q 20
Router(config-subif)#ip address 10.10.20.1 255.255.255.0

Router(config-subif)#interface FastEthernet0/0.99
%LINK-5-CHANGED: Interface FastEthernet0/0.99, changed state to up
Router(config-subif)#encapsulation dot1Q 99
Router(config-subif)#ip address 10.10.99.1 255.255.255.0
```

Configuramos los DHCP para cada clase para que los dispositivos del avion obtengan una direccion IP automaticamente:

```text
Router(config)#ip dhcp excluded-address 10.10.10.1 10.10.10.10
Router(config)#ip dhcp excluded-address 10.10.20.1 10.10.20.10
Router(config)#ip dhcp excluded-address 10.10.99.1 10.10.99.10

Router(config)#ip dhcp pool Turista
Router(dhcp-config)#network 10.10.10.0 255.255.255.0
Router(dhcp-config)#default-router 10.10.10.1
Router(dhcp-config)#dns-server 10.10.100.10

Router(config)#ip dhcp pool Business
Router(dhcp-config)#network 10.10.20.0 255.255.255.0
Router(dhcp-config)#default-router 10.10.20.1
Router(dhcp-config)#dns-server 8.8.8.8

Router(config)#ip dhcp pool Admin
Router(dhcp-config)#network 10.10.99.0 255.255.255.0
Router(dhcp-config)#default-router 10.10.99.1
Router(dhcp-config)#dns-server 8.8.8.8
```

Configuramos las NAT solo para VLAN20 (Business) permitiendo la salida a Internet, y marcamos las interfaces NAT en FE0/0:

```text
Router(config)#access-list 20 permit 10.10.20.0 0.0.0.255
Router(config)#ip nat inside source list 20 interface FastEthernet0/1 overload

Router(config)#interface FastEthernet0/0.10
Router(config-subif)#ip nat inside
Router(config)#interface FastEthernet0/0.20
Router(config-subif)#ip nat inside
Router(config)#interface FastEthernet0/0.99
Router(config-subif)#ip nat inside
```

Bloqueamos Internet a VLAN10 (Turista) usando una lista de control de acceso, dejando solo el acceso al server local:

```text
Router(config)#access-list 100 deny ip 10.10.10.0 0.0.0.255 any
Router(config)#access-list 100 permit ip any any
Router(config)#interface FastEthernet0/0.10
Router(config-subif)#ip access-group 100 out
```

Configuramos la ruta por defecto hacia ISP:

```text
Router(config)#ip route 0.0.0.0 0.0.0.0 200.0.0.2
```

Y finalmente configuramos el puerto FastEthernet0/1 y su interfaz NAT:

```text
Router(config)#interface FastEthernet0/1
Router(config-if)#no shutdown
%LINK-5-CHANGED: Interface FastEthernet0/1, changed state to up
Router(config-if)#ip nat outside
```

#### Configuracion Switch

Creamos tres VLANs segun la tabla de enrutamiento:

```text
Switch>enable
Switch#configure t
Switch(config)#vlan 10
Switch(config-vlan)#name Turista
Switch(config)#vlan 20
Switch(config-vlan)#name Business
Switch(config)#vlan 99
Switch(config-vlan)#name Admin
```

Configuramos el enlace hacia el router como trunk:

```text
Switch(config)#interface FastEthernet0/1
Switch(config-if)#switchport mode trunk
```

Asignamos los puertos a cada VLAN:

```text
Switch(config-if)#interface range FastEthernet0/2-3
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 10
Switch(config-if)#interface range FastEthernet0/4-5
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 20
Switch(config-if)#interface range FastEthernet0/6
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 99
Switch(config-if)#interface range FastEthernet0/7
Switch(config-if-range)#switchport mode access
Switch(config-if-range)#switchport access vlan 99
```

Y podemos observar la configuracion:

<img width="562" height="226" alt="image" src="https://github.com/user-attachments/assets/2d3c6996-cad1-4fb5-b658-8552223a4eb5" />

#### Configuracion Server

En el server utilizamos el servicio HTTP que viene por defecto, con un documento HTML para simular el servicio:

```html
<html> 
  <h1>🎬 AirConnect Entertainment</h1> 
  <p>Bienvenido a bordo. Disfrute nuestras películas y música.</p> 
</html> 
```

Y configuramos una IP estatica para el server:

<img width="698" height="268" alt="image" src="https://github.com/user-attachments/assets/eb426d95-e309-4507-811b-3e9ae35e9a74" />

#### Pruebas

- Ping al Servidor de Mantenimiento (Turista) --> Deberia responder ✔️

<img width="434" height="229" alt="image" src="https://github.com/user-attachments/assets/fe2ee5a0-c902-4a7d-b0c3-b00ae0fad38e" />

- Acceso HTTP a Servidor Local (Turista) --> Deberia cargar la pagina ✔️

<img width="702" height="219" alt="image" src="https://github.com/user-attachments/assets/7e14acb3-c166-41ad-9f54-f1be91f913f8" />

- Ping a Internet (Turista) --> Deberia responder ❌

<img width="452" height="195" alt="image" src="https://github.com/user-attachments/assets/20bd44e2-6988-4936-9fa4-dc928c2721c2" />

- Acceso HTTP a Servidor Local (Business) --> Deberia cargar la pagina ✔️

<img width="466" height="222" alt="image" src="https://github.com/user-attachments/assets/4a56b5b3-a7cc-4092-a06d-a90d1ad13ce9" />

- Ping a Internet (Business) --> Deberia responder ✔️

<img width="435" height="237" alt="image" src="https://github.com/user-attachments/assets/375c004d-3a0a-4b64-a825-5c41b8884aa3" />

- Ping entre Admin y Todos --> Deberia responder ✔️

<img width="430" height="209" alt="image" src="https://github.com/user-attachments/assets/dc4c5ee6-3ab1-4be5-b24e-a2b32eb61e03" />

<img width="429" height="221" alt="image" src="https://github.com/user-attachments/assets/735a21a5-188c-4ecf-8f04-5d09171ae48a" />

<img width="430" height="227" alt="image" src="https://github.com/user-attachments/assets/95c223c6-1c8c-48d2-bbdc-70a5b842f44a" />

<img width="473" height="221" alt="image" src="https://github.com/user-attachments/assets/8fe4c5e5-f7f0-4900-a866-b35473f6d772" />

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
