"""send ___ to ___ w/ scapy"""
from scapy.all import *
START_SEQUENCE = 132
MAX_PORT = 1024

port = 20

open_ports =""
ip_address = "127.0.0.1"

while port < MAX_PORT:
    syn_segment = TCP(dport = port, seq=START_SEQUENCE, flags='S')
    syn_packet = IP(dst=ip_address) / syn_segment
    send(syn_packet)
    syn_ack_packet = sr1(syn_packet, timeout=1)
    if syn_ack_packet is not None:
        open_ports += str(port) + ", "
    port+=1
print("open ports are :" + open_ports)