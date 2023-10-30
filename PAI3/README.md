# SSII-PAI3

## Uso
1. Descarga el proyecto y instala las dependencias especificadas en requirements.txt globalmente o en un entorno virtual con el siguiente comando:
```
pip install - r requirements.txt
```

2. Es importante modificar el HOST (la dirección ip) tanto en el servidor (serversocket.py) como en el cliente (clientsocket.py) para que el cliente pueda encontrar al servidor.
Para lanzar el cliente y el servidor del mismo ordenador, usa la dirección ip del localhost en ambos programas: 127.0.0.1
Para lanzar el cliente y el servidor de ordenadores distintos, usa la dirección IP del ordenador del servidor en el red local (En Windows se puede encontrar en el terminal con el comando "ipconfig" y leer la siguiente dirección ip: "Wireless LAN adapter WiFi") en ambos programas. Es necesario que el cliente y el servidor esten conectados al mismo red local.

3. Primero lanza el servidor en un terminal, entra la clave PEM (1234) y después lanza el programa del cliente en otro terminal y se abrirá la interfaz gráfica de usuario con la que se puede enviar mensajes secretos con credenciales proporcionados. 