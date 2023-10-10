# serversocket.py

import socket, pickle

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3030  # Port to listen on (non-privileged ports are > 1023)
HMAC = "SHA256"

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
            print(data_variable.print())
            data_string = pickle.dumps(data_variable)
            conn.send(data_string)
            # conn.sendall(data)
