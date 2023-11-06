# serversocket.py
import socket, pickle, hmac, hashlib, logging, json, threading
import ssl
from message import Message
from response_message import Response_Message

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)

HMAC = "SHA256"
KEY = 24  # ejemplo

#NONCES = []
NONCES_FILE = "nonces.json"

THREADS = 0

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

users = {
    "Jule": "Password",
    "Carou": "1234",
    "Scotti": "Scotti1"
}

def main():
    initialize_log()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        with context.wrap_socket(s, server_side=True) as ssock:
            print(f'Server listening on tcp:{HOST}:{PORT}')
            while True:
                conn, addr = ssock.accept()
                # create new thread to handle the client connection
                t = threading.Thread(target=handle, args=(conn, addr))
                t.start()

def handle(conn, addr):
        global THREADS 
        THREADS += 1
        print(f"Thread-{THREADS} {addr} is now connected")
        while True:
                data = conn.recv(1024)
                if not data:
                    continue
                data_variable = pickle.loads(data)
                if type(data_variable) == Message:
                    m = data_variable
                    m.print()
                    # verificar nonce
                    is_correct_nonce = check_nonces(m.get_nonce())
                    # verificar mac
                    is_integrate = check_mac(m)
                    # ini
                    if not all([is_correct_nonce, is_integrate]):
                        add_log_entry(m, is_correct_nonce, is_integrate)
                    is_auth = check_credentials(m.get_username(), m.get_password())
                    response = Response_Message(is_integrate, is_correct_nonce, is_auth)

                    data_string = pickle.dumps(response)
                    conn.send(data_string)
        conn.close()


def check_credentials(username, password):
    if username not in users.keys():
        return False
    if users[username] != password:
        return False
    return True

def check_nonces(nonce):
    try:
        with open(NONCES_FILE, "r") as file:
            NONCES = json.load(file)
    except FileNotFoundError:
        NONCES = []
    if nonce in NONCES:
        return False
    else:
        NONCES.append(nonce)
        with open(NONCES_FILE, "w") as file:
            json.dump(NONCES, file)
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


def initialize_log():
    log_format = '%(asctime)s - %(message)s'
    logging.basicConfig(filename='logfile.log', filemode='a', format=log_format, level=logging.INFO)
    logging.info("Session started.")


def add_log_entry(message, is_correct_nonce, is_integrate):
    if not is_integrate:
        logging.info("ERROR: %s. Transaction is not integrate. Different HMAC.", message.format_data())
    if not is_correct_nonce:
        logging.info("ERROR: %s. Transaction is not integrate. Nonce has already been used.", message.format_data())


main()