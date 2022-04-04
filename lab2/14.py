import socket

if __name__ == '__main__':
    host = '212.182.24.236'
    port = 2909

    datagram = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 " \
               "6c 6c 6f 20 3a 29 "

    datagram_split = datagram.split(' ')
    source = datagram_split[0] + datagram_split[1]
    destination = datagram_split[2] + datagram_split[3]
    data = ''

    for i in range(32, len(datagram_split)):
        data += datagram_split[i]

    output = f'zad13odp;src;{int(source, 16)};dst;{int(destination, 16)};data;{bytes.fromhex(data).decode("utf-8")}'
    print(source)
    print(destination)
    print(data)
    print(output)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(5)

        if s.connect_ex((host, port)) == 0:
            print('Connected')

            s.sendall(bytes(output, 'UTF-8'))
            recvData = s.recv(1024)

            print(f'Answer: {recvData.decode()}')
        else:
            print('Connection error')
