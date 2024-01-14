import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 8201))
print ("Server is up")
(client_name, client_address) = server_socket.recvfrom(1024)
data = client_name.decode()
print ("DATA RECIEVED")
response = "Hello " + data
server_socket.sendto(response.encode(), client_address)
server_socket.close()