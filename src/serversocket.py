# serversocket.py

import socket, pickle, hmac, hashlib
from message import Message
from response_message import Response_Message

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)

HMAC = "SHA256"
KEY = 24  # ejemplo

NONCES = []


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                data_variable = pickle.loads(data)

                if type(data_variable) == Message:
                    m = data_variable
                    m.print()
                    # verificar nonce
                    is_correct_nonce = check_nonces(m.get_nonce())
                    # verificar mac
                    is_integrate = check_mac(m)
                    response = Response_Message(is_integrate, is_correct_nonce)

                    data_string = pickle.dumps(response)
                    conn.send(data_string)


def check_nonces(nonce):
    if nonce in NONCES:
        return False
    else:
        NONCES.append(nonce)
        return True


def check_mac(message):
    original_mac_hex = message.get_mac()
    full_message = message.string_entire_message()
    # convert into bytes to use hmac libary
    key = bytes([KEY])
    full_message_bytes = full_message.encode('utf-8')
    #if HMAC == 'SHA256':
    hash_algorithm = hashlib.sha256
    new_hmac_hex = hmac.new(key, full_message_bytes, hash_algorithm).hexdigest()
    return original_mac_hex == new_hmac_hex


main()