import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',2000))
server.listen(5)
# server.settimeout(1)


while True:
    conn, addr = server.accept()
    print(conn,addr)
    while True:
        data = conn.recv(1024)
        if data.decode() == "" or  data.decode() == 'exit':
            break
        
        print("receive "+data.decode())
        
    
    conn.close()