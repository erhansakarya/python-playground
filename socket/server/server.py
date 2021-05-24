import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        messageLength = conn.recv(HEADER).decode(FORMAT)
        if messageLength:
            messageLength = int(messageLength)
            message = conn.recv(messageLength).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {message}")
            conn.send("message received.".encode(FORMAT))
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