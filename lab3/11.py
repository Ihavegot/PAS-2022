import socket
import re

HOST = '127.0.0.1'
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Server running on {HOST}:{PORT}")

    while True:
        data, client = s.recvfrom(1024)
        print(f'1. {data.decode("utf-8")}')

        if not re.match("zad15odpA;ver;[0-9]+;srcip;((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]);dstip;((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]);type;[0-9]+", data.decode('utf-8')):
            s.sendto(str.encode("BAD_SYNTAX"), client)
        elif data.decode('utf-8') == "zad15odpA;ver;4;srcip;212.182.24.27;dstip;192.168.0.2;type;6":
            s.sendto(str.encode("TAK"), client)
        else:
            s.sendto(str.encode("NIE"), client)

        data, client = s.recvfrom(1024)
        print(f'2. {data.decode("utf-8")}')

        if not re.match("zad15odpB;srcport;[0-9]+;dstport;[0-9]+;data;.+", data.decode('utf-8')):
            s.sendto(str.encode("BAD_SYNTAX"), client)
        elif data.decode('utf-8') == "zad15odpB;srcport;2900;dstport;47526;data;network programming is fun":
            s.sendto(str.encode("TAK"), client)
        else:
            s.sendto(str.encode("NIE"), client)