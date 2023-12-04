# PAI5
El objetivo de este proyecto es desarrollar una arquitectura de software en Android Studio para una cadena hotelera internacional que permita a los distintos centros hoteleros de todo el mundo realizar pedidos de material a través de dispositivos móviles.

## Manual para el uso facil
El proyecto consta de dos modulos seperados, el cliente como aplicación de Android y el servidor como proyecto maven. 
Por lo tanto es necesario ejecutar ambos proyectos simultaneamente y de manera separada en un entorno que soporte las necesidades. Nosotros usamos 
Android Studio para el cliente y Intellij para el servidor (Es imprescindible la necesidad de Maven para el utilizo de JDBC para la base de datos). 

1. Ejecuta el programa del servidor en Intellij o otro entorno que soporte maven. Main.java está fijado como clase principal a ejecutar en la configuración de maven. En la consola se podrá ver que el servidor se habrá iniciado y estará epserando una conección.
2. Ejecuta la MainActivity del la aplicación de Android del cliente y espera hasta que se abra el interfaz.
3. Desde aqui se podrán enviar peticiones proporcionando los datos necesarios y la identificación del empleado.
   -> El servidor tienes dos empleados en su base de datos, uno de número 111 y de lo cual tiene la clave publica correcta guardada e otro de numero 8 con una clave publica aleatoria.
4. En el fichero report.txt se podrá encontrar la cuota de envíos correctos a envíos totales y la tendencia comparada con los meses anteriorers de cada mes (en nuestro caso minutos).
