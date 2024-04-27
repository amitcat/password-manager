import socket
import select
import threading
from settings import *
from Crypto.PublicKey import RSA




class MultiThreadedClient(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.username = ""
        self.messages = ""
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stop_flag = threading.Event() # Event to signal thread termination
        self.client_encryption = Encryption()
        self.server_public_key = ""
        
    
    def run(self):
        client_thread = threading.Thread(target=self.connect)
        client_thread.start()

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")
        message = self.client_socket.recv(SERVER_BUFFER_SIZE)
        self.server_public_key = RSA.import_key(message)
        self.client_socket.sendall(self.client_encryption.export_public_key())
        self.client_recive()
        

    def disconnect(self):
        print("Client disconnected")
        self.stop_flag.set() # Set the stop flag to signal thread termination
        self.client_socket.close()


    def send_message(self, data):
        command = data[0]
        message = '|||'.join(data)
        encrypted_message = self.client_encryption.encrypt_msg(message.encode(), self.server_public_key)
        self.client_socket.send(str(len(encrypted_message)).zfill(8).encode())
        self.client_socket.sendall(encrypted_message)
        
        if command == 'exit':
            self.client_socket.close()

        
    # def client_recive(self):
    #     rlist, wlist, elist = select.select([self.client_socket],[],[])

    #     for current_socket in rlist:

    #         length = int(current_socket.recv(8).decode())
    #         message = current_socket.recv(length)
    #         print(f'RECIEVED MESSAGE: {message}')
    #         decrypted_message = self.client_encryption.decrypt(message)
    #         print(f'DECRYPTED MESSAGE: {decrypted_message}')
    #         self.messages = decrypted_message
    #         print(f'DEBUG: {self.messages}')

            # except:
            #     print('byebye')
            #     self.client_socket.close()
            #     break

    def client_recive(self):
        while True:
            try:
                length = int(self.client_socket.recv(8).decode())
                message = self.client_socket.recv(length)
                print(f'RECIEVED MESSAGE: {message}')
                decrypted_message = self.client_encryption.decrypt_msg(message)
                print(f'DECRYPTED MESSAGE: {decrypted_message}')
                self.messages = decrypted_message
                print(f'DEBUG: {self.messages}')
                # message = self.client_socket.recv(SERVER_BUFFER_SIZE)
                # print(message)
                # decrypted_message = self.client_encryption.decrypt(message)
                # self.messages = decrypted_message
                # print (decrypted_message)
            except:
                print('byebye')
                self.client_socket.close()
                break
    