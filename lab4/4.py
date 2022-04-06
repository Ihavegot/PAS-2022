import datetime
import socket

PORT = 2900
BUFFSIZE = 1024000


def tcpServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(1)

    print(f"Server tcp running on localhost:{PORT}")

    while True:
        clientSocket, (host, rport) = s.accept()
        while True:
            data = clientSocket.recv(BUFFSIZE)
            if not data:
                break
            del data
        clientSocket.close()
        print(f'Host: {host}, port: {rport}')


def udpServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', PORT))

    print(f"Server udp running on localhost:{PORT}")

    while True:
        data, client = s.recvfrom(BUFFSIZE)
        if not data:
            break
        del data

        print('Done with', client[0], 'port', client[1])
    s.close()


tcpServer()
# udpServer()
