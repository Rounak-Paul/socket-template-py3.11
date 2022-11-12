import socket

IP = 'hub'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print ("Socket successfully created")
    
    s.connect((IP, PORT))        
    print ("socket connected to %s" %(PORT))

    s.send("Test".encode())
    data = s.recv(1024)
    print(data.decode())

    s.close()