import socket
import threading
import time

class Socket_Message():
    def __init__(self):
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!DISCONNECT'
    def msg_format(self,msg):
            message = msg.encode(self.FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(self.FORMAT)
            send_length += b' ' * (self.HEADER-len(send_length))
            return send_length, message

class Socket_Server(Socket_Message):
    def __init__(self,IP,PORT,func):
        super().__init__()
        self.event = threading.Event()
        self.IP = IP
        self.PORT = PORT
        hostname = socket. gethostname()
        local_ip = socket. gethostbyname(hostname)
        self.server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.IP, self.PORT))  
        self.func = func      
        print (f'[STATUS] socket binded to {local_ip}:{self.PORT}')
        
    def handle_client(self,conn,addr):
        print(f'[STATUS] New connection from: {addr}')
        self.event.set()
        while self.event.is_set():
            data = f'{self.func()}'
            msg_length, msg = super().msg_format(data)
            conn.send(msg_length)
            # print(len(msg_length))
            # time.sleep(5)
            conn.send(msg)
            print('[SERVER] data sent')
        print('[SERVER] Closing Thread')
        conn.close()
        
    def close_conn(self):
        print('[SERVER] Closing connection...')
        self.event.clear()
        time.sleep(0.5)
        print('[SERVER] Releasing port...')
        self.server.close()
        time.sleep(0.5)
        print('[SERVER] Exiting...')
        
        
    def start(self):
        self.server.listen()
        print(f"[STATUS] Listening to port: {self.PORT}")
        try:
            while True:
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn,addr))
                thread.start()
                print(f'[THREAD] Active threads: {threading.activeCount() - 1}')
        except KeyboardInterrupt:
            try:
                self.close_conn()
            except:
                print('[SERVER] No Active Connections. Exiting...')

import random
def generate_int():
    return random.randint(0,10)

def main():
    print("[STATUS] Starting server ...")
    serv = Socket_Server(IP='',PORT=2001,func=generate_int)
    serv.start()
    
main()