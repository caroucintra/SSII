# clientsocket.py

import socket, pickle, hmac, hashlib
from message import Message
from response_message import Response_Message

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server

HMAC = "SHA256"
KEY = 24  # ejemplo


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            # Reemplazar por el input de GUI
            print("Enter the amount: ")
            amount = input()
            m = Message("L", "R", amount)

            # eligir nonce y añadir al mensaje con add_nonce()
            m.add_nonce(create_unique_nonce())
            # crear mac con la función HMAC a base del mensaje con nonce (conseguido por la función string_entire_message()) y añadir lo al mensaje con add_mac(mac)
            m.add_mac(create_mac(m.string_entire_message))

            data_string = pickle.dumps(m)
            s.send(data_string)

            data = s.recv(1024)
            data_variable = pickle.loads(data)
            if type(data_variable) == Response_Message:
                response = data_variable
                response.print()


def create_unique_nonce():
    # a implementar
    return "example nonce"


def create_mac(message_and_nonce):
    # convert into bytes to use hmac libary
    key = bytes([KEY])
    message_and_nonce_bytes = message_and_nonce.encode('utf-8')
    #if HMAC == 'SHA256':
    hash_algorithm = hashlib.sha256
    hmac_resumen_hex = hmac.new(key, message_and_nonce_bytes, hash_algorithm).hexdigest()
    return hmac_resumen_hex

main()