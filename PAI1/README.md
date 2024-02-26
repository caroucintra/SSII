# Host Intrusion Detection Sytem (HIDS)

## Uso
1. Descarga el proyecto y instala las dependencias especificadas en requirements.txt globalmente o en un entorno virtual con el siguiente comando:
```
pip install - r requirements.txt
```

2. En la función scan_all_files() en el fichero scan.py la ruta se especifica como path + "/**". Sin embargo, dependiendo del sistema operativo, la ruta se indica como "\**". Si el programa no encuentra el sistema de ficheros que has especificado, intenta cambiarlo.

3. Ejecuta el fichero __main__.py y configura el programa a tus necesidades.Asegurate que la ruta local al sistema de ficheros exista en tu ordenador y que el correo electronico sea valido.

### Notas
- La ruta al sistema de ficheros se puede especificar como ruta relativa (con el directorio SSII-PAI1 como raíz) o como ruta absoluta. 
- Para probar el programa, es aconsejable ajustar manualmente los tiempos del scheduling para el escaneo y la notificación por correo electrónico en el main.py a los intervalos deseados.