# clientsocket.py

import socket, pickle, hmac, hashlib, datetime, concurrent.futures, threading, time
import ssl
from message import Message
from response_message import Response_Message

import gui
hostname = 'ST8'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='cert.pem')

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

HMAC = "SHA256"
KEY = 24  # ejemplo

BOT_NUM = 1


def setParams(user, pas, msj):
    global usuario, contrasena, mensaje
    if (user != ""):
        usuario = user
    else:
        usuario = "L"
    if (pas != ""):
        contrasena = pas
    else:
        contrasena = "R"
    if (msj != ""):
        mensaje = msj
    else:
        mensaje = '0'


def main():
    #start_client_gui()
    for i in range(300):
        i = threading.Thread(target=start_client_bot)
        i.start()



def start_client_gui():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with context.wrap_socket(s, server_hostname=hostname) as ssock:
            ssock.connect((HOST, PORT))
            while True:
                running = gui.startGUI()
                if running == False:
                    break
                setParams(gui.usuario_input, gui.contrasena_input, gui.mensaje_input)
                m = Message(usuario, contrasena, mensaje)

                # eligir nonce y añadir al mensaje con add_nonce()
                m.add_nonce(create_unique_nonce())
                print('nonce: '+m._nonce)
                
                #prueba: replay
                #m.add_nonce("1234")
                
                # crear mac con la función HMAC a base del mensaje con nonce (conseguido por la función string_entire_message()) y añadir lo al mensaje con add_mac(mac)
                m.add_mac(create_mac(m.string_entire_message()))

                #prueba: man in the middle
                #m._mensaje += "0"

                data_string = pickle.dumps(m)
                ssock.send(data_string)

                data = ssock.recv(1024)
                data_variable = pickle.loads(data)
                if type(data_variable) == Response_Message:
                    response = data_variable
                    response_msg = response.print()
                    running = gui.showResults(response_msg)


def start_client_bot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with context.wrap_socket(s, server_hostname=hostname) as ssock:
            ssock.connect((HOST, PORT))
            while True:
                m = Message("Jule", "Password", "Test Message")

                # eligir nonce y añadir al mensaje con add_nonce()
                m.add_nonce(create_unique_nonce())
                print('nonce: '+m._nonce)
                # crear mac con la función HMAC a base del mensaje con nonce (conseguido por la función string_entire_message()) y añadir lo al mensaje con add_mac(mac)
                m.add_mac(create_mac(m.string_entire_message()))

                data_string = pickle.dumps(m)
                ssock.send(data_string)

                data = ssock.recv(1024)
                data_variable = pickle.loads(data)
                if type(data_variable) == Response_Message:
                    response = data_variable
                    response.print()
                time.sleep(30)
                        

# devuelve la fecha y hora actuales al milisegundo exacto
def create_unique_nonce():
    present = datetime.datetime.now()
    # tiempo en milisegundos
    nonce = present.strftime("%Y%m%d%H%M%S%f")[:-3]
    return nonce


def create_mac(message_and_nonce):
    # convert into bytes to use hmac libary
    key = bytes([KEY])
    message_and_nonce_bytes = message_and_nonce.encode('utf-8')
    #if HMAC == 'SHA256':
    hash_algorithm = hashlib.sha256
    hmac_resumen_hex = hmac.new(key, message_and_nonce_bytes, hash_algorithm).hexdigest()
    return hmac_resumen_hex

main()