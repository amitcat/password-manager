import socket
from msvcrt import getch, kbhit
import select
import sys

from settings import *


def send_message(soc: socket.socket, username: str, action: int, data: bytes) -> None:
    soc.send(str(len(uname)).zfill(USERNAME_MAX_NUM_DIGITS).encode())
    soc.send(username.encode())
    soc.send(str(action).encode())
    soc.send(str(len(data)).zfill(DATA_MAX_NUM_DIGITS).encode())
    soc.send(data)


# get initial data for protocol
uname = input("Enter your username: ")


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("127.0.0.1", SERVER_PORT))
action = input("What action: ")

data = b''
while True:
    rlist, wlist, elist = select.select([socket], [socket], [])


    if kbhit():
        key = getch()
        if key != b'\r':
            sys.stdout.write(key.decode())
            sys.stdout.flush()
            data += key

        else:
            if data == b'exit':
                send_message(socket, uname, action, data)
                print('\nyou left the chat')
                socket.close()
                break
            if socket in wlist:
                send_message(socket, uname, action, data)
                print()
                data = b''
    if socket in rlist:
        msg = socket.recv(SERVER_BUFF_SIZE)
        print(msg.decode())
