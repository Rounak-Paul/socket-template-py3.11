import socket
import threading

HEADER = 64
IP = ''
PORT = 2001
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))        
print ("socket binded to %s" %(PORT))

def handle_client(conn,addr):
    print(f'[STATUS] New connection from: {addr}')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}] {msg}')
            conn.send("[SERVER] msg recieved".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[STATUS] Listening to port: {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f'[THREAD] Active threads: {threading.activeCount() - 1}')

print("[STATUS] Starting server ...")
start()
