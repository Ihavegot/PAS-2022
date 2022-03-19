import socket

if __name__ == '__main__':
    host = '212.182.24.236'
    port = 2908
    mess = 'test message'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        if s.connect_ex((host, port)) == 0:
            print('Connected')

            if len(mess) > 20:
                s.sendall(bytes(mess[:20], 'UTF-8'))
            else:
                s.sendall(bytes("{:<20}".format(mess), 'UTF-8'))
            recvData = s.recv(1024)

            print(f'Answer: {recvData.decode()}')
        else:
            print('Connection error')
