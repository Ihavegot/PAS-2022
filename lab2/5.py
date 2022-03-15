import socket

if __name__ == '__main__':
    host = '212.182.24.27'
    port = 22

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(5)
            if s.connect_ex((host, port)) == 0:
                print('Connected')
                mess = input('User message: ')

                s.sendall(bytes(mess, 'UTF-8'))
                recvData = s.recv(1024)

                print(recvData.decode())

                if input('Do you want to quit?\nYES or NO y/n\n') == 'y':
                    break
            else:
                print('Connection error')
