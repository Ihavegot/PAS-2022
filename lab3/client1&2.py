import socket

HOST = '127.0.0.1'
PORT = 2900
mess = 'test message'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)
    if s.connect_ex((HOST, PORT)) == 0:
        print('Connected')

        s.sendall(bytes(mess, 'UTF-8'))
        recvData = s.recv(1024)

        print(f'Answer: {recvData.decode()}')
    else:
        print('Connection error')