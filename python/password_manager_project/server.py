import socket
import select

from settings import *
from server_utils import *


# def get_all_users_fromDB (uname, password):


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    database = Database()
    database.create_user_table()
    database.create_password_to_webs_table()

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
                client_data = current_socket.recv(SERVER_BUFFER_SIZE).decode()
                print(f'BEBUG: {client_data}')
                command , username , password = client_data.split(":")
                if command == 'exit':
                    print(f'closing connection with {current_socket}')
                    client_sockets.remove(current_socket)
                    wlist.remove(current_socket)
                    current_socket.close()
                    break
                if command == 'login':
                    print('login command')
                    pass
                if command == 'signup':
                    message = database.insert_user(username,password)
                    
                    print('signup command')
                    pass

                
                    
                
                # else:
                #     print('good job')


if __name__ == "__main__":
    main()
