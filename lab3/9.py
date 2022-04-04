import socket
import re

HOST = '127.0.0.1'
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    print(f"Server running on {HOST}:{PORT}")

    while True:
        data, client = s.recvfrom(1024)
        print(data.decode('utf-8'))

        if not re.match("zad14odp;src;[0-9]+;dst;[0-9]+;data;.+", data.decode('utf-8')):
            s.sendto(str.encode("BAD_SYNTAX"), client)
        elif data.decode('utf-8') == "zad14odp;src;60788;dst;2901;data;programming in python is fun":
            s.sendto(str.encode("TAK"), client)
        else:
            s.sendto(str.encode("NIE"), client)