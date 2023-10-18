# clientsocket.py

import socket, pickle, hmac, hashlib, datetime
from message import Message
from response_message import Response_Message
import time

import gui
import thread

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

HMAC = "SHA256"
KEY = 24  # ejemplo


def setParams(ori, dest, amo):
    print(ori, dest, amo)
    global origin, destination, amount
    if (ori != ""):
        origin = ori
    else:
        origin = "L"
    if (dest != ""):
        destination = dest
    else:
        destination = "R"
    if (amo != ""):
        amount = int(amo)
    else:
        amount = 0


def startClient():
    print('a ser chamado')
    print(origin, destination, amount)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            # Reemplazar por el input de GUI
            #print("Enter the amount: ")
            #amount = input()
            #
            m = Message(origin, destination, amount)

            # eligir nonce y añadir al mensaje con add_nonce()
            m.add_nonce(create_unique_nonce())
            # crear mac con la función HMAC a base del mensaje con nonce (conseguido por la función string_entire_message()) y añadir lo al mensaje con add_mac(mac)
            m.add_mac(create_mac(m.string_entire_message))
            print('client cenas 1')

            data_string = pickle.dumps(m)
            s.send(data_string)

            data = s.recv(1024)
            print('client cenas')
            data_variable = pickle.loads(data)
            if type(data_variable) == Response_Message:
                response = data_variable
                response.print()


# devuelve la fecha y hora actuales al milisegundo exacto
def create_unique_nonce():
    present = datetime.datetime.now()
    # milliseconds son suficiente?
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

if __name__ =="__main__":
    # creating thread

    t1 = thread.MyThread(gui.startGUI())
    t2 = thread.MyThread(startClient)
 
    t1.join()
    t2.join()
 
    # both threads completely executed
    print("Done!")