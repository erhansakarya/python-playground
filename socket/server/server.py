import socket
import threading
import json
from json import JSONEncoder

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        messageLength = conn.recv(HEADER).decode()
        if messageLength:
            messageLength = int(messageLength)
            message = conn.recv(messageLength).decode()
            if message == DISCONNECT_MESSAGE:
                connected = False
            else:
                received = json.loads(message)
                print("command:" + received["command"])
                print("message:" + received["message"])
            print(f"[{addr}] {message}")
    conn.close()
    print(f"[{addr}] connection closed")


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server...")
start()