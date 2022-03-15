import socket
import sys

if __name__ == "__main__":

    host = '212.182.24.27'
    port = 25
    remote_server_ip = socket.gethostbyname(host)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)

        if s.connect_ex((remote_server_ip, port)) == 0:
            print(f"Conected on port: {port} - {socket.getservbyport(port, 'tcp')}")
        else:
            print("Not conected")