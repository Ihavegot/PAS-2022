import socket

if __name__ == '__main__':
    host = '212.182.24.27'
    port = 22
    hostname = 'google.com'

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)
        if s.connect_ex((host, port)) == 0:
            print('Connected')

            s.sendall(bytes(hostname, 'UTF-8'))
            recvData = s.recv(1024)

            print(f'Answer: {recvData.decode()}')
        else:
            print('Connection error')
