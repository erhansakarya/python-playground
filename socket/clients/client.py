import socket

SERVER = "192.168.1.5"
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message):
    message = message.encode(FORMAT)
    messageLength = len(message)
    sendLengthMessage = str(messageLength).encode(FORMAT)
    sendLengthMessage += b' ' * (HEADER - len(sendLengthMessage))
    client.send(sendLengthMessage)
    client.send(message)
    
send("Merhaba!")
send("Hello!")
send(DISCONNECT_MESSAGE)