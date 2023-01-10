import socket

HEADER = 64
IP = '192.168.11.140'
PORT = 2001
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

while True:
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)
        print(msg)
