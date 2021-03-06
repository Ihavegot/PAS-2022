import socket

if __name__ == '__main__':
    host = '212.182.24.236'
    port = 2901
    mess = 'test message'

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        if s.connect_ex((host, port)) == 0:
            print('Connected')

            s.sendall(bytes(mess, 'UTF-8'))
            recvData = s.recv(1024)

            print(f'Answer: {recvData.decode()}')
        else:
            print('Connection error')
