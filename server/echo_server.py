import socket
import threading

IP = ''
PORT = 2001

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))        
print ("socket binded to %s" %(PORT))

def handle_client(conn,addr):
    print(f'[STATUS] New connection from: {addr}')

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f'[THREAD] Active threads: {threading.activeCount() - 1}')

print("[STATUS] Starting server ...")
start()
