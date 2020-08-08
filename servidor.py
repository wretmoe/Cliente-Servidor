import socket

#Standard loopback interface address (localhost)
HOST = '127.0.0.1'

#Port to listen on (non-privileged ports are > 1023)
PORT = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Servidor escuchando por el puerto 10000")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)