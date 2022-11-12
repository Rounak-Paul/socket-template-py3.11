import socket

HEADER = 64
IP = 'hub'
PORT = 2000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)

send('test from client')
send(DISCONNECT_MESSAGE)