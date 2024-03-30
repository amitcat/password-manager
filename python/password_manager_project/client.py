import socket
import threading
from settings import *



class MultiThreadedClient(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.username = ""
        self.messages = []
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.stop_flag = threading.Event() # Event to signal thread termination
    
    def run(self):
        client_thread = threading.Thread(target=self.connect)
        client_thread.start()

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")
        self.client_recive()
        

    def disconnect(self):
        print("Client disconnected")
        self.stop_flag.set() # Set the stop flag to signal thread termination
        self.client_socket.close()


    def send_message(self, data):
        print(data)
        command = data[0]            
        info = data[1]
        message =f'{command}:{info}'
        print (type(data))
        self.client_socket.send(message.encode())
        if command == 'exit':
            self.client_socket.close()

        if command == 'signin':
            pass

        if command =='signup':
            pass
        
        



    def client_recive(self):
        while True:
            try:
                message = self.client_socket.recv(SERVER_BUFFER_SIZE).decode()
                print (message)
            except:
                print('byebye')
                self.client_socket.close()
                break
    