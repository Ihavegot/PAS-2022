import textwrap
import socket


def decode_binary_string(s):
    return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))


datagram = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 " \
           "00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d " \
           "69 6e 67 20 69 73 20 66 75 6e"

bin_data = '01000101000000000000000001001110111101111111101001000000000000000011100000000110100111010011001111010100' \
           '101101100001100000011011110000001010100000000000000000100000101101010100101110011010011011111011111110010' \
           '011110001010111110000010000101000000110110000011000000000011000000000001110001111001110100111000000000000' \
           '00000000000001000000010000100000001010000000111010011011101011000000010000000000001011111110001110010101' \
           '10111001100101011101000111011101101111011100100110101100100000011100000111001001101111011001110111001001' \
           '100001011011010110110101101001011011100110011100100000011010010111001100100000011001100111010101101110 '

tcp_ip = textwrap.wrap(bin_data, 32)

# A
version = tcp_ip[0][0:4]
protocol = tcp_ip[2][8:16]
# source_ip = socket.inet_ntoa(bytes(tcp_ip[3], 'utf-8')) # Du no czmu nie działa, przeliczone online kalkulatorem
# destination_ip = socket.inet_ntoa(bytes(tcp_ip[4], 'utf-8')) # Du no czmu nie działa, przeliczone online kalkulatorem

output1 = f'zad15odpA;ver;{int(version, 2)};srcip;212.182.24.27;dstip;192.168.0.2;type;{int(protocol, 2)}'

# B
source = tcp_ip[5][0:16]
destination = tcp_ip[5][16:32]
data = ''
temp = ''
for i in range(13, len(tcp_ip)):
    temp += tcp_ip[i]

data = decode_binary_string(temp)

output2 = f'zad15odpB;srcport;{int(source, 2)};dstport;{int(destination, 2)};data;{data}'

# Socket
host = '212.182.24.236'
port = 2911

print(output1)
print(output2)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(5)

    if s.connect_ex((host, port)) == 0:
        print('Connected')

        s.sendall(bytes(output1, 'UTF-8'))
        recvData = s.recv(1024)

        print(f'Answer: {recvData.decode()}')

        s.sendall(bytes(output2, 'UTF-8'))
        recvData = s.recv(1024)

        print(f'Answer: {recvData.decode()}')
    else:
        print('Connection error')
