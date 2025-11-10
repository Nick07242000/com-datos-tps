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

### 1) Alcance de Redes y Virtualización


### a) Clasificacion de las redes según su cobertura geografica:

| Tipo de Red                       | Acrónimo | Alcance típico        | Características principales                                               | Tecnologías / Ejemplos                                     |
|----------------------------------|:--------:|------------------------|---------------------------------------------------------------------------|------------------------------------------------------------|
| Red de Área Personal             | **PAN**  | Hasta ~10 m            | Conecta dispositivos personales cercanos; bajo consumo y fácil conexión. | Bluetooth, NFC; celular + auriculares inalámbricos         |
| Red de Área Local                | **LAN**  | Hasta ~1 km            | Alta velocidad; usada en edificios, aulas u oficinas.                     | Ethernet, Wi-Fi; red de computadoras de un aula            |
| Red de Campus                    | **CAN**  | Hasta ~10 km           | Interconecta varias LAN dentro de un campus o empresa.                    | Fibra óptica; red de todos los edificios de una universidad |
| Red de Área Metropolitana        | **MAN**  | 10–50 km               | Conecta múltiples redes dentro de una ciudad.                             | Enlaces metropolitanos, MPLS; sedes municipales conectadas  |
| Red de Área Amplia               | **WAN**  | > 100 km (global)      | Interconecta redes a nivel nacional o internacional.                      | Internet, VPNs, fibra submarina, satélite                  |
| Red de Área Local Inalámbrica    | **WLAN** | Hasta ~100 m           | Variante inalámbrica de la LAN; ofrece movilidad.                         | Wi-Fi (IEEE 802.11); Wi-Fi doméstico                        |
| Red de Área Amplia Inalámbrica   | **WWAN** | 1–1000 km o más        | Cobertura amplia mediante redes celulares o satelitales.                  | 4G, 5G, Starlink, NB-IoT                                   |
| Red de Almacenamiento            | **SAN**  | Limitada al data center| Red dedicada exclusivamente al intercambio de datos de almacenamiento.    | Fibre Channel, iSCSI; Centros de datos empresariales        |


### b) VLAN (Virtual Local Area Network)
Una VLAN es una red lógica que permite dividir una red física (como la de un switch) en múltiples redes virtuales independientes, sin necesidad de modificar el cableado ni la infraestructura. Cada VLAN forma un dominio de broadcast propio, por lo que los dispositivos dentro de una misma VLAN pueden comunicarse entre sí, pero no con los de otras VLAN a menos que exista un router o switch de capa 3 que realice inter-VLAN routing.

### Ventajas:
| Ventaja          | Descripción                                                                 |
|------------------|-----------------------------------------------------------------------------|
| Seguridad         | Aísla el tráfico entre grupos, evitando accesos no autorizados.            |
| Flexibilidad      | Permite reasignar usuarios sin modificar cableado físico.                  |
| Mejor rendimiento | Reduce el tamaño del dominio de broadcast, disminuyendo tráfico excesivo. |
| Escalabilidad     | Facilita la expansión y reorganización de la red.                          |

### Clasificacion:
| Tipo de VLAN                | Descripción                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Port-based VLAN             | Cada puerto del switch se asigna manualmente a una VLAN.                    |
| MAC-based VLAN              | Se asigna la VLAN según la dirección MAC del dispositivo.                   |
| Protocol-based VLAN         | Clasifica el tráfico según el protocolo utilizado (IP, IPX, AppleTalk).     |
| Network-based VLAN (IP)     | Determina la VLAN en función de la subred IP del dispositivo.               |

### VLANs especiales:
| VLAN              | Función                                                                               |
|------------------|---------------------------------------------------------------------------------------|
| VLAN 1            | VLAN por defecto, usada inicialmente para administración básica y control del switch. |
| VLAN nativa       | Transporta tramas sin etiqueta (untagged) en enlaces trunk.                           |
| VLAN de gestión   | VLAN dedicada a la administración de dispositivos de red (ejemplo: VLAN 99).         |

---------------------------
### c) Protocolo IEEE 802.1Q y su relación con las VLAN


**IEEE 802.1Q** es el estándar que define cómo se identifican y transportan **VLANs** a través de redes Ethernet. Permite que varias redes lógicas compartan la misma infraestructura física sin perder el aislamiento entre ellas.

En lugar de tener un cable o switch por cada red, 802.1Q  etiqueta las tramas Ethernet para indicar a qué VLAN pertenecen, haciendo posible que un solo enlace físico (enlace **trunk**) transporte tráfico de múltiples VLANs.


### ¿Cómo se relaciona con las VLAN?

Gracias a 802.1Q se puede:

- **Permitir comunicación entre VLANs** usando un router o switch capa 3.
- **Transportar múltiples VLANs** por un solo enlace físico (modo trunk).
- **Identificar** a qué VLAN pertenece cada trama.
- **Mantener separado el tráfico** entre distintas VLANs, aunque compartan el mismo cable o switch.


Sin este estándar, las VLAN solo funcionarían dentro de un mismo switch.

---
### d)  ¿Qué es el Tagging?

**Tagging** es el proceso mediante el cual un switch **inserta una etiqueta (tag) 802.1Q** en una trama Ethernet para indicar **a qué VLAN pertenece**.  
Este mecanismo permite que **múltiples VLANs compartan un mismo enlace físico** sin perder el aislamiento lógico del tráfico.

Sin el tagging, todas las tramas que viajan entre switches serían indistinguibles y no sería posible mantener separadas las VLANs en enlaces troncales.


**¿Cómo funciona?**

1. Una trama llega al switch por un **puerto de acceso**, asociado a una VLAN.
2. Si la trama debe ser enviada a otro switch mediante un **enlace trunk**, el switch **agrega una etiqueta 802.1Q** con el **VLAN ID (VID)**.
3. La trama viaja por el enlace trunk con esa etiqueta.
4. El switch receptor **lee la etiqueta**, identifica la VLAN y reenvía la trama solo a los puertos correspondientes.
5. Si el puerto destino es de acceso, **se elimina la etiqueta (untagging)** antes de entregar la trama al dispositivo final.



***Tipos de puertos involucrados***

| Tipo de puerto | Tramas etiquetadas | Función principal | Ejemplo de uso |
|----------------|:-----------------:|------------------|----------------|
| **Access Port** | No (tramas van sin tag) | Conecta dispositivos finales a una sola VLAN. | PC, impresora, cámara IP. |
| **Trunk Port** | Sí (tramas llevan tag 802.1Q) | Transporta tráfico de múltiples VLANs entre equipos de red. | Conexión entre switches o switch-router. |


---
### Topologia Packet Tracer

Se implementa la siguiente topología de red en packet tracer:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/a5a8a3e3-96fd-462c-a6c9-33c210329beb" />

<img width="600" alt="image" src="https://github.com/user-attachments/assets/f50f3b95-5e31-489c-b783-66f81533caca" />

Con la siguiente tabla de ruteo:

<img width="400" alt="image" src="https://github.com/user-attachments/assets/0c678316-76fc-42c8-ae11-e4442e87ae5c" />

a) En cada computadora se ingresa a la terminal y se cambian los nombres de los switches a SW-1 y SW-2 respectivamente desde la configuración global por medio de los siguientes comandos:

```
Switch>enable
Switch#configure terminal
Switch(config)#hostname SW-1
```

b) Se asignan contraseñas para cada modo en cada uno de los switches:

Para EXEC User desde config-line:
```
SW-1(config)#line console 0
SW-1(config-line)#password contrasena_consola
SW-1(config-line)#login
SW-1(config-line)#exit
```

Nota: login es usado para habilitar el acceso

Para EXEC Privilegiado: 
```
SW-1(config)#enable secret contrasena_exec
```
Para acceso remoto (Telnet o SSH):
```
SW-1(config)#line vty 0 15
SW-1(config-line)#password contrasena_vty
SW-1(config-line)#login
```

c) Para el siguiente paso se encriptan las contraseñas (que no lo están ya) con un cifrado débil pero solo en el archivo de configuración, no mientras se envían por los medios. Se utiliza el siguiente comando desde la config global:

```
SW-1(config)#service password-encryption
```

Y se puede verificar que funcionó al ir a exec privilegiado e ingresar el siguiente comando:
```
SW-1#show running-config
```
<img width="400" alt="image" src="https://github.com/user-attachments/assets/87789924-17e7-49da-8aa0-8ff7c4fb10a2" />

<img width="400" alt="image" src="https://github.com/user-attachments/assets/1c2cd3c4-1469-435c-a8ec-4899f1911fec" />

d) Una vez que se tienen todos los accesos protegidos con contraseñas, se prosigue a configurar las direcciones con la tabla de ruteo antes provista. Para esto se configuran las redes VLAN para ambos switch:

```
SW-1(config)#interface vlan 1
SW-1(config-if)#ip address 192.168.10.11 255.255.255.0
SW-1(config-if)#no shutdown
SW-1(config-if)#

%LINK-5-CHANGED: Interface Vlan1, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up

SW-1(config-if)#exit
```

Nota: no shutdown habilita la interfaz virtual.

Con ```show ip interface brief``` se puede ver las interfaces que están conectadas:

<img width="500" alt="image" src="https://github.com/user-attachments/assets/cfeb29c1-7b95-4680-93b0-15d3977d4114" />

e) En este caso hay 3 UP y las 3 son necesarias. Fa0/1 es la interfaz que permite la conexión directa entre el switch a la PC y Fa0/2 permite la conexión entre ambos switches y la Vlan1 es la interfaz que une la red.

Si se quisiera deshabilitar una interfaz porque no se usa, se tendría que ir a esa interfaz y usar el comando ```shutdown``` para inhabilitarla administrativamente.

f) Para guardar las configuraciones realizadas, se usa el comando ```write memory``` (equivale a ```copy running-config startup-config```).

g) Para probar las conexiones entre las PC se usó ```ping <ip de la otra pc>```:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/f85d18a0-2c9a-4994-b12c-f9a10de26ede" />

<img width="300" alt="image" src="https://github.com/user-attachments/assets/6e58d75c-a70c-4dcb-96d7-2ddfe6bb6182" />

<img width="300" alt="image" src="https://github.com/user-attachments/assets/81e8d56f-5e34-42f7-8e02-63c2f2af210b" />

Pero se tuvo que modificar la ip de las vlan a 192.168.10.11 y 192.168.10.12 para que todos los dispositivos estén en la misma red y no tener que agregar un router.

h) Se crean VLANs en ambos switches:

```
sw1(config)# vlan 10
sw1(config-vlan)# name Laboratorio
sw1(config-vlan)# vlan 20
sw1(config-vlan)# name Bar
sw1(config-vlan)# vlan 99
sw1(config-vlan)# name Management
sw1(config-vlan)# end
```

i) 
<img width="600" alt="image" src="https://github.com/user-attachments/assets/f19093db-c758-49cc-a3d2-08e032857e59" />

La VLAN por defecto es la VLAN 1.

j) Se asigna el puerto f0/6 de la PC-A a la VLAN Laboratorio (vlan 10), esto implica que este puerto ahora será un punto de acceso a VLAN Laboratorio:

```
SW-1#config t
Enter configuration commands, one per line. End with CNTL/Z.
SW-1(config)#interface f0/6
SW-1(config-if)#switchport mode access
SW-1(config-if)#switchport access vlan 10
```

k) Desde la VLAN 1, remover la ip de Management y configurarla para funcionar en la VLAN 99 (que configuramos como Management). Esto se hace ya que usar VLAN 1 para administración es una mala práctica de seguridad. Esta tiene todos los puertos activos por defecto y se usa para muchas funciones internas. Por esto, dejar la IP de management ahí la hace vulnerable y accesible desde cualquier puerto del switch.
Con este ejercicio se pretende que la VLAN 99 se vuelva una red de administración aislada, donde solo los administradores pueden conectarse a configurar el switch.

```
sw1(config)# interface vlan 1
sw1(config-if)# no ip address
sw1(config-if)# interface vlan 99
sw1(config-if)# ip address 192.168.10.11 255.255.255.0
sw1(config-if)# end
```

l) Verificar el estado de la VLAN utilizando show vlan brief y el estado de las interfaces
utilizando show ip interface brief. Colocar los output en el informe e interpretar.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/b8726e74-111a-4469-a3bc-ff6108e971ba" />

Aquí se puede ver los puertos físicos asociados a los diferentes puertos y como la VLAN 1 está asociada a todos. También como se asoció el puerto Fa0/6 para que solo este esté asociado a la VLAN Laboratorio (10) que se creó con anterioridad.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/03fffc06-434d-4a5b-a424-2350fb7ef533" />

Como vemos en la imagen anterior, la ip de la VLAN 1 se borró y se agregó una ip en la VLAN 99 (Management), por lo cual ahora la ip de administración está ahí en donde solo puede ser accedida por los puertos que se asocien a esta red, la cual todavía no tiene puertos asignados al ver down en Protocol. 

m) Se asigna la PC-B a la VLAN Laboratorio (10) en el sw2.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/2a0b6e5e-e724-49e0-98d7-36c97f0a7d4d" />

Sigue down en Protocol porque no se asignó todavía un puerto físico a esta red (Se le asignó el fa0/6 pero en la PC-A). 

n) Verificar la conectividad entre PC-A y PC-B utilizando pings.

Conexión entre PC-A y PC-B: 

<img width="700" alt="image" src="https://github.com/user-attachments/assets/48da9629-51fc-4efb-aceb-2b0cf61af57b" />

Conexión entre PC-B y PC-A:

<img width="600" alt="image" src="https://github.com/user-attachments/assets/7cba55c6-242f-451f-bb84-b1ce18f15f01" />

Nota: se tuvo que asignar los puertos fa0/1 y fa0/2 a las nuevas VLANs de admin ya que sino no se podían comunicar.

Conexión entre SW-2 y SW-1:

<img width="500" alt="image" src="https://github.com/user-attachments/assets/718bc6c6-8f2d-46d2-80e4-0de9e7c4e5e0" />


Conexión entre SW-1 y SW-2:

<img width="500" alt="image" src="https://github.com/user-attachments/assets/0315f25e-3da2-4260-8656-0c032b166149" />

Gracias a los pings se puede determinar que tanto las PCs como los switch están conectados correctamente entre ellos ya que con este comando se prueba el envio de mensajes y la recepcion entre un dispositivo y el otro.

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
