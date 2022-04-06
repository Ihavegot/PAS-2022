from random import randint
import socket, select
from time import gmtime, strftime

HOST = '127.0.0.1'
PORT = 2912
flag = False

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)
randomnumber = randint(1, 100)

print ("[%s] TCP RANDOM NUMBER Server is waiting for incoming connections on port %s ... " % (strftime("%Y-%m-%d "
                                                                                                       "%H:%M:%S",
                                                                                                       gmtime()),
                                                                                              PORT))
print ("[%s] Random number is now %s " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), randomnumber))

while True:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

            print ("[%s] Client %s connected ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))

        else:
            try:
                data = sock.recv(1024)
                if data:

                    try:
                        num = int(data)
                        print ("[%s] Client %s tries ... %s ... " % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address, num))

                        if num == randomnumber :
                            randomnumber = randint(1, 100)
                            msg = "You won! This is the right number!"
                            print ("[%s] Client %s figured out the number!" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))
                            sock.sendall(msg.encode("UTF-8"))
                            flag = True
                            break
                        elif num < randomnumber:
                            msg = "Try again with a bigger number!"
                            sock.sendall(msg.encode("UTF-8"))

                        elif num > randomnumber :
                            msg = "Try again with a lower number!"
                            sock.sendall(msg.encode("UTF-8"))

                    except Exception:
                        msg = "Na-ah! Wrong type! %s"
                        sock.sendall(msg.encode("UTF-8"))
            except Exception:
                print ("[%s] Client (%s) is offline" % (strftime("%Y-%m-%d %H:%M:%S", gmtime()), client_address))
                sock.close()
                connected_clients_sockets.remove(sock)
                continue
        if flag:
            break
    if flag:
        break
server_socket.close()