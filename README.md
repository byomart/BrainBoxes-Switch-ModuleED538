# BrainBoxes-Switch

## Módulo ED-538
 
El dispositivo ED-538 de BrainBoxes es un multiconmutador con 8 entradas digitales y 4 salidas. 

<p align="center">
<img width="150" alt="Módulo ED-538" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/9608af6e-dcb6-4f5d-a421-265ff34dba2c">
</p>

## Puesta en marcha del módulo ED-538

### Configuración IP

Leyendo el manual del fabricante vemos que el propio dispositivo dispone de una API, por lo que comenzamos conectándonos por cable Ethernet al dispositivo, forzando la dirección de nuestro equipo dentro de la red establecida por defecto para el propio conmutador (192.168.127.254). Así pues, le damos a nuestro equipo una dirección para que llegue al dispositivo, por ejemplo la 192.168.127.17. Una vez en la misma red, podemos abrir la API del módulo escribiendo su dirección IP en el navegador web, y se muestra la siguiente pestaña, en la que podemos modificar a nuestro gusto la dirección IP del dispositivo.

<p align="center">
<img width="750" alt="Configuración IP del módulo ED-538" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/0c08e4ed-5f44-4d2b-94a9-54986a4f9094">
</p>


### Control de salidas por API

A fin de controlar las salidas del conmutador, vamos a crear una serie de endpoints que se explican de forma detallada más adelante.

<p align="center">
<img width="750" alt="Configuración IP del módulo ED-538" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/6db2a66c-4ef5-4f43-a3fc-b809cf488938">
</p>

a) **Encender una salida**

  En este caso, para encender una salida debemos cerrar dicha salida y así favorecer el paso corriente. Las dos imágenes siguientes muestran el correcto funcionamiento del endpoint (_encender_RL0_) así como el RL0 cerrado.

<p align="center">
<img width="750" alt="enceneder_salida(abrir)" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/3e309883-3a19-44af-98bf-4492ea9670f3">
</p>

<p align="center">
<img width="750" alt="RL0 cerrado" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/215b4e83-d9af-4251-b4b4-626e8ab46b7a">
</p>

  
b) **Apagar salida**

  En este caso, para apagar una salida debemos dejarla abierta y así no habrá paso de corriente. Las dos imágenes siguientes muestran el correcto funcionamiento del endpoint (_apagar_RL0_) así como el RL0 abierto.

<p align="center">
<img width="750" alt="apagar_salida(abrir)" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/d1efd45d-5d9f-4a20-9e25-8e0d06af4107">
</p>


<p align="center">
<img width="750" alt="RL0 abierto" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/bae4a23a-237b-4849-9dc7-e57eac0a6346">
</p>




c) **Encender/Apagar varias salidas**

A modo de ejemplo, vamos a cerrar 3/4 salidas de forma simultánea. En este caso, especificamos mediante el endpoint que las salidas a cerrar son: 0, 1 y 3. En la segunda imagen se puede observar como únicamente el RL2 queda abierto. 

<p align="center">
<img width="750" alt="especificar_accion" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/8cd23b80-dc46-4f54-91bf-262d4089ba0f">
</p>


<p align="center">
<img width="750" alt="0,1,2 cerrados" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/2e1bfd04-aa98-45c2-b65d-4b0feaba264b">
</p>


d) **Listar todas las posibles combinaciones sobre las cuatro salidas**

Para mayor facilidad de uso, listaremos todas las acciones posibles a realizar sobre las cuatro salidas disponibles. Bastará con tomar una opción de esta lista e introducirla en el endopoint anterior para especificar la acción deseada para las salidas.

<p align="center">
<img width="750" alt="Listar acciones" src="https://github.com/fbayomartinez/BrainBoxes-switch/assets/163590683/87e73e5d-df70-4a21-9d31-14f896b480db">
</p>


Por último, destacamos que las acciones a realizar sobre las salidas se llevan a cabo mediante instrucciones ASCII configuradas a partir del manual del fabricante.

