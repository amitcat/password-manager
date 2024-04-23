import socket
import select

from settings import *
from server_utils import *
import time
# start

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
        self.client_public_key = {}
        self.client_symetric_keys = {}
        self.CIPHER ={}
        print(f"Server listening on port {SERVER_PORT}...")
        self.messages = []  
        self.client_sockets = []

    def send_messages(self):
        for message , client_addr, receivers in self.messages:
            for receiver in receivers:
                if receiver in self.wlist:
                    # print('dic', self.client_public_key)
                    # print('receivers', receivers)
                    # print('receiver', receiver)
                    # print('client_addr', client_addr)
                    cipher = self.format_message(message, client_addr)
                    # print('cipher', cipher)
                    receiver.send(str(len(cipher)).zfill(8).encode())
                    receiver.sendall(cipher)
                    receivers.remove(receiver)
                    print('>>>>>>',self.messages)
            if not receivers:
                self.messages.remove((message , client_addr , receivers))
                print('remove',self.messages)

        # for command , username , password , web_name , password_for_web ,new_password_for_web , receivers in self.messages:
        #     for receiver in receivers:
        #         if receiver in self.wlist:
        #             print('1')
        #             cipher = self.format_message(command , username , password , web_name , password_for_web ,new_password_for_web, receiver)
        #             print('2')
        #             receiver.send(str(len(cipher)).zfill(8).encode())
        #             print('3')
        #             receiver.sendall(cipher)
        #             print('4')
        #             receivers.remove(receiver)
        #             print('>>>>>>',self.messages)
        #     if not receivers:
        #         self.messages.remove((command , username , password , web_name , password_for_web ,new_password_for_web , receivers))
        #         print('>>>>>>',self.messages)
    # def format_message(self, command , username , password , web_name , password_for_web ,new_password_for_web , receiver):
    #     print('123',receiver, self.client_public_key)
    #     message = f'{command}|||{username}|||{password}|||{web_name}|||{password_for_web}|||{new_password_for_web}'.encode()
    #     cipher = self.encryption.encrypt(message, self.client_public_key[receiver])
    #     return cipher
    def format_message(self, message , receiver):
        cipher = self.encryption.encrypt_msg(message.encode(), self.client_public_key[receiver])
        return cipher
    
    def recvall(self, sock: socket.socket, size: int) -> bytes:
        received_chunks = []
        buf_size = 1024
        remaining = size
        while remaining > 0:
            received = sock.recv(min(remaining, buf_size))
            if not received:
                raise Exception('unexpected EOF')
            received_chunks.append(received)
            remaining -= len(received)
        return b''.join(received_chunks)
    def run(self):
        while True:
            self.rlist, self.wlist, self.elist = select.select([self.server_socket] + self.client_sockets, self.client_sockets, [])
            
            for current_socket in self.rlist:
                if current_socket is self.server_socket:
                    client_conn, client_addr = self.server_socket.accept()
                    print(f"{client_addr} just joined!")
                    self.client_sockets.append(client_conn)
                    server_public_key = self.encryption.export_public_key()
                    client_conn.sendall(server_public_key)
                    self.client_public_key[client_addr] = RSA.import_key(client_conn.recv(self.server_buffer_size))
                    
                else:
                    if current_socket in self.rlist:
                        length = int(current_socket.recv(8).decode())
                        client_data = self.recvall(current_socket, length)
                        decrypted_client_data = self.encryption.decrypt_msg(client_data)
                        # print(f'DEBUG: {decrypted_client_data}')
                        command , username , password , web_name , password_for_web ,new_password_for_web = decrypted_client_data.split("|||")

                        if command == 'exit':
                            print(f'closing connection with {current_socket}')
                            self.client_sockets.remove(current_socket)
                            self.wlist.remove(current_socket)
                            current_socket.close()
                            break

                        if command == 'signup':
                            print('signup command')
                            message = self.database.insert_user(username,password)
                            print("OUTPUT: >>>>> " + str(message))
                            self.messages.append((message,client_addr,[current_socket]))
                            # self.messages.append((command , username , password , web_name , password_for_web ,new_password_for_web , [client_addr]))
                            # encrypted_message = self.encryption.encrypt(message, self.client_public_key[client_addr])
                            # current_socket.send(encrypted_message)
                            
                        if command == 'login':
                            print('login command')
                            message = self.database.login_into_the_system(username,password)
                            print("OUTPUT: >>>>> " + str(message))
                            # print('current sockeet',current_socket)
                            # print('client addr',client_addr)
                            self.messages.append((message,client_addr,[current_socket]))
                            # self.messages.append((command , username , password , web_name , password_for_web ,new_password_for_web , [client_addr]))
                            # encrypted_message = self.encryption.encrypt(message, self.client_public_key[client_addr])
                            # current_socket.send(encrypted_message)
                            
                        if command == 'insert web and password':
                            print('insert web name and password command')
                            message = self.database.insert_web_name_and_password(username, web_name, password_for_web)
                            print("OUTPUT: >>>>> " + str(message))
                            self.messages.append((message,client_addr,[current_socket]))
                            # self.messages.append((command , username , password , web_name , password_for_web ,new_password_for_web , [client_addr]))
                            # encrypted_message = self.encryption.encrypt(message, self.client_public_key[client_addr])
                            # current_socket.send(encrypted_message)
                            

                        if command =='update password for web':
                            print('update password for web command')
                            message = self.database.update_password_for_web(username, web_name, password_for_web, new_password_for_web, self.encryption)
                            print("OUTPUT: >>>>> " + str(message))
                            self.messages.append((message,client_addr,[current_socket]))
                            # self.messages.append((command , username , password , web_name , password_for_web ,new_password_for_web , [client_addr]))
                            # encrypted_message = self.encryption.encrypt(message, self.client_public_key[client_addr])
                            # current_socket.send(encrypted_message)

                        if command =='show password by web':
                            print('show password by web command')
                            message = self.database.show_password_by_web(username, web_name, self.encryption, self.client_public_key[client_addr])
                            print("OUTPUT: >>>>> " + str(message))
                            self.messages.append((message,client_addr,[current_socket]))
                            
                        if command == 'remove web and password':
                            print('remove web and password command')
                            message = self.database.delete_web_and_password(username, web_name)
                            print("OUTPUT: >>>>> " + str(message))
                            self.messages.append((message,client_addr,[current_socket]))

                    else:
                        print(f'closing connection with {current_socket}')
                        self.client_sockets.remove(current_socket)
                        self.wlist.remove(current_socket)
                        current_socket.close()
                        break

            self.send_messages()



if __name__ == "__main__":
    server = Server(SERVER_IP, SERVER_PORT, SERVER_BUFFER_SIZE)
    server.run()