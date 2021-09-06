# Control Remoto Robot Limpia playas 2021

Programas necesarios para el correcto funcionamiento del robot limpiaplayas a control remoto.

Probablemente sirva como base para el proyecto final del TMR.

## Descripcion

Actualmente cuenta con el codigo dividido en varias clases en distintos archivos, en la version final se espera que todos los codigos de prueba esten implementados en los programas rpc_server y client.

El cliente controla al servidor (raspberry pi 3) a traves de un control remoto usando como medio un servidor rpc, el usuario tiene acceso a la informacion obtenida por los sensores, asi como controlar los motores y la camara por medio de un control de Xbox conectado a la computadora cliente.

## Getting Started

### Dependencies

En el raspberry que sirve como servidor.
- Python > 3.6
- OpenCV 4
- PySerial
- NumPy
- RPi.GPIO

En la computadora cliente.
- Python > 3.6
- PyGame - Utilizado para captar el contol
- Control conectado a USB - Testeado con control de Xbox One conectado a USB

### Installing

- Git clone el repositorio

### Executing program

En el raspberry que sirve como servidor.
```
python3 rpc_server.py
```

En la computadora cliente.

```
python3 rpc_client.py
```

Si se desea hacer algun debugeo o alguna prueba de sensores o de serial se recomienda ejecutar el archivo en solitario.

ex.
```
python3 Motors.py
python3 ArduinoSerialComm.py
```

## Authors

Agustin Zavala 

[@AgusZavala](https://discord.com/users/468214034722848799)


## Acknowledgments

Este proyecto cuenta con la colaboracion del Dr. Ruben Machucho Cadena, sin sus aportes muchos avances no podrian haber sido cumplidos.

