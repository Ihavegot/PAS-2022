import socket

if __name__ == '__main__':
    host = '212.182.24.236'
    port = 2910

    datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 " \
               "75 6e "

    datagram_split = datagram.split(' ')
    source = datagram_split[0] + datagram_split[1]
    destination = datagram_split[2] + datagram_split[3]
    data = ''

    for i in range(8, len(datagram_split)):
        data += datagram_split[i]

    # print(source)
    # print(destination)
    # print(data)

    output = f'zad14odp;src;{int(source, 16)};dst;{int(destination, 16)};data;{bytes.fromhex(data).decode("utf-8")}'

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)

        if s.connect_ex((host, port)) == 0:
            print('Connected')

            s.sendall(bytes(output, 'UTF-8'))
            recvData = s.recv(1024)

            print(f'Answer: {recvData.decode()}')
        else:
            print('Connection error')
