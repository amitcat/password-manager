import socket
import threading
from settings import *

MY_IP = '127.0.0.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((MY_IP, SERVER_PORT))

def client_send():
    while True:
        message = input(f'>>>>')
        client.send(message.encode())
        if message== 'exit':
            print('bye bye')
            client.close()
            break

def client_recive():
    while True:
        try:
            message = client.recv(SERVER_BUFFER_SIZE).decode()
            print (message)
        except:
            print('error')
            client.close()
            break

def main():
   

    send_thread = threading.Thread(target=client_send)
    send_thread.start()

    # receive_thread = threading.Thread(target=client_recive)
    # receive_thread.start()

if __name__ == "__main__":
    main()
