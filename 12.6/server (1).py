import socket
import select
from dataclasses import dataclass
from datetime import datetime

from settings import *


@dataclass
class Message:
    uname: bytes
    action: int
    data: bytes


def recv_message(soc: socket.socket, name_socket_dict: dict) -> Message:
    uname_len = int(soc.recv(USERNAME_MAX_NUM_DIGITS))
    uname = soc.recv(uname_len)
    if uname not in name_socket_dict.keys():  # super inefficient but simple
        name_socket_dict[uname] = soc
    action = int(soc.recv(1))
    param_len = int(soc.recv(DATA_MAX_NUM_DIGITS))
    param = soc.recv(param_len)

    return Message(uname, action, param)


def send_message(message, wlist: list[socket.socket]):
    for soc in wlist:
        if soc != message[0]:
            soc.send(message[1])


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", SERVER_PORT))
server_socket.listen()
print("server is listening...")

client_sockets = []
messages = []
managers = ['bob', 'amit']

name_socket_dict = {}

while True:
    rlist, wlist, elist = select.select([server_socket] + client_sockets, client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            client_conn, client_addr = current_socket.accept()
            print(f"{client_addr} just joined!")
            client_sockets.append(client_conn)
        else:
            client_message = recv_message(current_socket, name_socket_dict)
            print(f"DEBUG: {client_message}")
            if client_message.data == b"exit":
                print(f"closing connection with {client_message.uname}")
                client_sockets.remove(current_socket)
                wlist.remove(current_socket)
                current_socket.close()
                messages.append((None, b"Server: " + client_message.uname + b" has left the chat"))
                break
            elif client_message.action == 1:
                final_message = datetime.now().strftime("%H:%M:%S").encode() + \
                                b" " + client_message.uname + b': ' + client_message.data

                if client_message.data.decode()[0:2] == '/2':  # add manager
                    # print(client_message.uname.decode())
                    flag = True
                    for manager in managers:
                        if client_message.uname.decode() == manager:
                            managers.append(client_message.data.decode()[3:])
                            current_socket.send(f'you added {client_message.data.decode()[3:]} successfully'.encode())
                            flag = False
                    if flag:
                        current_socket.send(b'you dont have permission')
                # elif client_message.data.decode()[0:2] == '/3':  # kick client
                #
                # elif client_message.data.decode()[0:2] == '/4':  # mute client
                #
                # elif client_message.data.decode()[0:2] == '/5':  # privet message

                else:
                    messages.append((current_socket, final_message))

            # elif client_message.action == 2:
            #     user_to_remove = client_message.data
            #     for name in name_socket_dict:
            #         if name == user_to_remove:

            #             client_sockets.remove(name_socket_dict[name])
            #             name_socket_dict.pop(name)
            #             send_message((None, b"Server: " + user_to_remove + b" has been kicked"), wlist)
            #
    for message in messages:
        send_message(message, wlist)
        messages.remove(message)
