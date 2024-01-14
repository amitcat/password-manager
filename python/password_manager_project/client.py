import socket
import threading
from settings import *

MY_IP = '127.0.0.1'

def send_data(client):
    message = input('message>>>')
    client.send(message.encode())

    # Receive and print the server's response
    response = client.recv(1024)
    print(f"Received from server: {response.decode()}")
    
    # client.close()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((MY_IP, SERVER_PORT))
    
    client_thread = threading.Thread(target=send_data, args=(client,))
    client_thread.start()


if __name__ == "__main__":
    main()
