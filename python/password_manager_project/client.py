import socket, threading
from threading import Thread
from settings import *
from client_gui import *
import hashlib

class Client():
    def __init__(self) -> None:
        self.MY_IP = '127.0.0.1'
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.MY_IP, SERVER_PORT))
        self.gui = Client_gui()

    def signin(self):
        self.gui.log_in_screen()
        password = bytes(self.gui.pword, 'utf-8')
        hash_password = hashlib.sha256(password).hexdigest()
        unername_password = f'{self.gui.user}:{hash_password}'
        print(unername_password)
        self.client_socket.send(unername_password.encode())
        self.menu()

    def menu (self):
        self.gui.menu_page()



    def client_recive(self):
        while True:
            try:
                message = self.client_socket.recv(SERVER_BUFFER_SIZE).decode()
                print (message)
            except:
                print('error')
                self.client_socket.close()
                break

        

        # while True:
        #     self.client_send()
def main(self):
    # print('nice')
    send_thread = threading.Thread(target=self.signin)
    send_thread.start()


if __name__ == "__main__":
    #לקרוא לפעולות מהגוי
    # print('sdsd')
    current_client = Client()
    print(type(current_client.gui))
    main(current_client) #מעביר 


