import socket
from threading import Thread

from f1_2020_telemetry.packets import unpack_udp_packet

def switch(packet_id):
    if packet_id == 1 and session:
        print(Packet_Value1)
    elif packet_id == 2:
        print(Packet_Value2)
    elif packet_id == 5:
        print(Packet_Value3)

switch(61)

def GetData():
    check = True
    while check:
        udp_packet = udp_socket.recv(2048)
        packet = unpack_udp_packet(udp_packet)
        header = packet.header
        switch(header.packetId)

Packet_Value1 = (1, 'Session')
Packet_Value2 = (2, 'LapData')
Packet_Value3 = (5, 'CarSetups')

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)  
UDP_PORT = 20777
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind((IPAddr, UDP_PORT))

session = (True)

"""
The Thread() accepts many parameters. The main ones are:

target: specifies a function (GetData) to run in the new thread.
args: specifies the arguments of the function (GetData). The args argument is a tuple.

creo un nuovo thread per ricevere i dati
"""

get_data_thread = Thread(target=GetData)
# write_data_thread = Thread(target=WriteData,args=)
get_data_thread.start()
get_data_thread.join() # aspetta che ricevi i dati prima di continuare nell'esecuzione del programma (scrittura)
