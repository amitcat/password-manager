import socket
import select
import random

from settings import *
from datetime import date


def generate_password():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    symbols = '[]{}()*;/,._-'
    all_together = lower + upper + symbols
    pass_length = 16
    new_password = "".join(random.sample(all_together, pass_length))
    return new_password

def handle_client(client_socket):
    # Code to handle a specific client
    request = client_socket.recv(SERVER_BUFFER_SIZE)
    print(f"Received from {client_socket.getpeername()}: {request.decode()}")

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
        rlist, wlist, elist = select.select([server_socket]+client_sockets, client_sockets, [])
        
        for current_socket in rlist:
            if current_socket is server_socket:
                client_conn, client_addr = server_socket.accept()
                print(f"Accepted connection from {client_addr}")
                rlist.append(client_conn)
            else:
                # Existing client has data
                data = current_socket.recv(1024)
                print(data.decode())
                if data:
                    handle_client(current_socket)
                else:
                    # No data, client closed the connection
                    print(f"Connection from {current_socket.getpeername()} closed.")
                    rlist.remove(current_socket)
                    current_socket.close()


if __name__ == "__main__":
    main()
