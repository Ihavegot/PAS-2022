import socket

if __name__ == "__main__":

    ip = '212.182.24.236'
    x, y = 2900, 2910
    remote_server_ip = socket.gethostbyname(ip)

    for i in range(x, y+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)

            if s.connect_ex((remote_server_ip, i)) == 0:
                print(f"Conected on port: {i} - {socket.getservbyport(i, 'tcp')}")
            else:
                print(f"Port {i} closed")