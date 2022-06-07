import socket
import time

HOST = '127.0.0.1'
PORT = 2900
BUFSIZE = 4096
count = 1000


def tcpClient():
    testdata = 'x' * (BUFSIZE - 1) + '\n'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect_ex((HOST, PORT))
        t1 = time.time()

        i = 0
        while i < count:
            i = i + 1
            s.send(bytes(testdata, 'utf-8'))

        s.shutdown(1)
        t2 = time.time()
        data = s.recv(BUFSIZE)

        print(data.decode('utf-8'))
        print(f'Time: {t2 - t1}')


def udpClient():
    testdata = 'x' * (BUFSIZE - 1) + '\n'
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect_ex((HOST, PORT))
        t1 = time.time()

        i = 0
        while i < count:
            i = i + 1
            s.send(bytes(testdata, 'utf-8'))

        s.shutdown(1)
        t2 = time.time()

        print(f'Time: {t2 - t1}')


# tcpClient()
udpClient()
