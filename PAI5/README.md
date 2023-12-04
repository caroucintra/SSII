# PAI5
El objetivo de este proyecto es desarrollar una arquitectura de software en Android Studio para una cadena hotelera internacional que permita a los distintos centros hoteleros de todo el mundo realizar pedidos de material a través de dispositivos móviles.

## Manual para el uso fácil
El proyecto consta de dos módulos separados, el cliente (archivo MyApplication) como aplicación de Android y el servidor (archivo Server) como proyecto Maven. 
Por lo tanto, es necesario ejecutar ambos proyectos simultáneamente y de manera separada en un entorno que soporte las necesidades. Nosotros usamos 
Android Studio para el cliente y Intellij para el servidor (Es imprescindible la necesidad de Maven para él utilizo de JDBC para la base de datos). 

1. Ejecuta el programa del servidor en Intellij o otro entorno que soporte Maven. Main.java está fijado como clase principal a ejecutar en la configuración de Maven. En la consola se podrá ver que el servidor se habrá iniciado y estará esperando una conexión.
2. Ejecuta la MainActivity de la aplicación de Android del cliente y espera hasta que se abra la interfaz.
3. Desde aquí se podrán enviar peticiones proporcionando los datos necesarios y la identificación del empleado.
   -> El servidor tienes dos empleados en su base de datos, uno de número 111 y de lo cual tiene la clave pública correcta guardada y otro de número 8 con una clave pública aleatoria.
4. En el fichero report.txt se podrá encontrar la cuota de envíos correctos a envíos totales y la tendencia comparada con los meses anteriores de cada mes (en nuestro caso minutos).
