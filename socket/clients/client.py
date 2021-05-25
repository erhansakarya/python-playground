import socket
import json
from json import JSONEncoder

SERVER = "192.168.1.5"
PORT = 5050
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(message):
    message = message
    messageLength = len(message)
    sendLengthMessage = str(messageLength)
    sendLengthMessage += " " * (HEADER - len(sendLengthMessage))
    client.send(sendLengthMessage.encode())
    client.send(message.encode())

def createCommandMessage(command, message):
    commandMessage = {"command":command, "message":message}
    return json.dumps(commandMessage)

send(createCommandMessage("create", "resource1"))
send(createCommandMessage("delete", "resource2"))
send(DISCONNECT_MESSAGE)