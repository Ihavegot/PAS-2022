import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)

    if s.connect_ex(('ntp.task.gda.pl', 13)) == 0:
        print(f'Connected\nCurrent date and time: {s.recv(1024).decode()}')
    else:
        print('Connection error')

    s.close()