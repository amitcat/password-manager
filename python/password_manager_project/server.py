import socket
import select

from settings import *
from server_utils import *
import time

class Server():
    def __init__(self, server_ip, server_port, server_buffer_size):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((server_ip, server_port))
        self.server_socket.listen()
        self.server_buffer_size = server_buffer_size

        self.database = Database()
        self.database.create_user_table()
        self.database.create_password_to_webs_table()

        self.encryption = Encryption()
        self.client_public_key = ""

        print(f"Server listening on port {SERVER_PORT}...")

        self.client_sockets = []

    def run(self):
        while True:
            rlist, wlist, elist = select.select([self.server_socket] + self.client_sockets, self.client_sockets, [])
            
            for current_socket in rlist:
                if current_socket is self.server_socket:
                    client_conn, client_addr = self.server_socket.accept()
                    print(f"{client_addr} just joined!")
                    self.client_sockets.append(client_conn)
                    # client_conn.send(b'hi')
                    server_public_key = self.encryption.export_public_key()
                    client_conn.sendall(server_public_key)
                    self.client_public_key = RSA.import_key(client_conn.recv(self.server_buffer_size))
                else:
                    try:
                        client_data = current_socket.recv(self.server_buffer_size)
                        print(f'BEBUG: {client_data}')
                        decrypted_client_data = self.encryption.decrypt(client_data)
                        print('1')
                        command , username , password , web_name , password_for_web ,new_password_for_web = decrypted_client_data.split("||")

                        if command == 'exit':
                            print(f'closing connection with {current_socket}')
                            self.client_sockets.remove(current_socket)
                            wlist.remove(current_socket)
                            current_socket.close()
                            break

                        if command == 'signup':
                            print('signup command')
                            message = self.database.insert_user(username,password)
                            print("OUTPUT: >>>>> " + str(message))
                            encrypted_message = self.encryption.encrypt(message, self.client_public_key)
                            current_socket.send(encrypted_message)
                            
                        if command == 'login':
                            print('login command')
                            message = self.database.login_into_the_system(username,password)
                            print("OUTPUT: >>>>> " + str(message))
                            encrypted_message = self.encryption.encrypt(message, self.client_public_key)
                            current_socket.send(encrypted_message)
                            
                        if command == 'insert web and password':
                            print('insert web name and password command')
                            message = self.database.insert_web_name_and_password(username, web_name, password_for_web)
                            print("OUTPUT: >>>>> " + str(message))
                            encrypted_message = self.encryption.encrypt(message, self.client_public_key)
                            current_socket.send(encrypted_message)
                            

                        if command =='update password for web':
                            print('update password for web command')
                            message = self.database.update_password_for_web(username, web_name, password_for_web, new_password_for_web, self.encryption)
                            print("OUTPUT: >>>>> " + str(message))
                            encrypted_message = self.encryption.encrypt(message, self.client_public_key)
                            current_socket.send(encrypted_message)

                        if command =='':
                            pass

                    except:
                        print(f'closing connection with {current_socket}')
                        self.client_sockets.remove(current_socket)
                        wlist.remove(current_socket)
                        current_socket.close()
                        break



if __name__ == "__main__":
    server = Server(SERVER_IP, SERVER_PORT, SERVER_BUFFER_SIZE)
    server.run()