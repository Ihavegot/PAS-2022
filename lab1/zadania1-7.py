import shutil

if __name__ == "__main__":
    shutil.copy(input("Plik 1: "), input("Plik 2: "))


import shutil

if __name__ == "__main__":
    shutil.copy(input("Image 1: "), input("Image 2: "))


import ipaddress


def check(addres):
    try:
        ip = ipaddress.ip_address(addres)
        print("IP address is ok")
    except ValueError:
        print("IP address is not ok")


if __name__ == "__main__":
    check(input("IP: "))


import socket

if __name__ == "__main__":
    print(f"Hostname: {socket.gethostbyaddr(input('IP: '))}")


import socket

if __name__ == "__main__":
    print(f"Hostname: {socket.gethostbyname(input('Hostname: '))}")

import socket
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        remote_server = sys.argv[1]
        remote_server_ip = socket.gethostbyname(remote_server)
        port = int(sys.argv[2])

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((remote_server_ip, port))

        if result == 0:
            print("Conected")
        else:
            print("Not conected")


import socket
import sys

if __name__ == "__main__":

    ip = input("IP: ")

    for i in range(65535):
        remote_server_ip = socket.gethostbyname(ip)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((remote_server_ip, i))

        if result == 0:
            print(f"Conected on port: {i}")
        else:
            print(f"Port {i} closed")