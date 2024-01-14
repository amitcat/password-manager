import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ("before send")
my_socket.sendto('stok'.encode(), ('127.0.0.1',8201))
print ("after send")
(data, remote_address) = my_socket.recvfrom(1024)
print('The server sent: ' + data.decode())
my_socket.close()
