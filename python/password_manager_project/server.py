import socket
import select
import random

from settings import *
from datetime import date

#region Functions
def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    symbols = '[]{}()*;/,._-'
    all_together = lower + upper + symbols
    pass_length = 16
    new_password = "".join(random.sample(all_together, pass_length))
    return new_password

#endregion

def handle_client(client_socket):
    request = client_socket.recv(SERVER_BUFFER_SIZE)
    print(f"Received from {client_socket}: {request.decode()}")

    # You can add more logic here to process the request

    # Send a response back to the client
    response = "Hello from the server!"
    client_socket.send(response.encode())

    # Close the client socket
    if request=='quit':
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    print(f"Server listening on port {SERVER_PORT}...")

    client_sockets = []

    while True:
        rlist, wlist, elist = select.select([server_socket] + client_sockets, client_sockets, [])
        
        for current_socket in rlist:
            if current_socket is server_socket:
                client_conn, client_addr = server_socket.accept()
                print(f"{client_addr} just joined!")
                client_sockets.append(client_conn)
            else:
                client_data = current_socket.recv(SERVER_BUFFER_SIZE)
                print(f'BEBUG: {client_data.decode()}')
                if client_data == b'exit':
                    print(f'closing connection with {current_socket}')
                    client_sockets.remove(current_socket)
                    wlist.remove(current_socket)
                    current_socket.close()
                    break
                else:
                    print('good job')


if __name__ == "__main__":
    main()
