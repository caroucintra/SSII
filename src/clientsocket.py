# clientsocket.py

import socket, pickle, message

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3030  # The port used by the server
HMAC = "SHA256"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print("Enter the amount: ")
        amount = input()

        m = message.Message("L", "R", amount)
        data_string = pickle.dumps(m)
        s.send(data_string)
        # s.sendall(b"Hello, world")
        data = s.recv(1024)
        data_variable = pickle.loads(data)
        print(data_variable.print())


# print(f"Received {data!r}")
