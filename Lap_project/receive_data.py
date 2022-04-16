import socket
import csv
from threading import Thread
from f1_2020_telemetry.packets import unpack_udp_packet

Packet_Value1 = (1, 'Session')
Packet_Value2 = (2, 'LapData') # ultimo giro con i settori un po' un casino, seleziona solo una macchina
Packet_Value3 = (5, 'CarSetups') # tipo tutto seleziona solo una macchina
Packet_Value4 = (6, 'CarStatusPacket') # benza e consumo gomme
header = ['weather', 'trackTemperaure', 'airTemperature']
playerCarId = None

def switch(packet_id, packet):
    if packet_id == 1:
        GetSessionData(packet)
    elif packet_id == 2:
        GetLapData(packet)
    elif packet_id == 5:
        GetCarSetup(packet)
    elif packet_id == 6:
        GetCarStatus(packet)

def GetData():
    check = True
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)  
    UDP_PORT = 20777
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_socket.bind((IPAddr, UDP_PORT))
    while check:
        udp_packet = udp_socket.recv(2048)
        packet = unpack_udp_packet(udp_packet)
        header = packet.header
        global playerCarId
        playerCarId = header.playerCarIndex
        switch(header.packetId,packet)

def GetSessionData(packet):
    # packet = packet.PacketSessionData controlla come accedere al ai dati della sessione
    weather = packet.weather
    trackTemperature = packet.trackTemperature
    airTemperature = packet.airTemperature
    sessionUID = packet.header.sessionUID
    sessionData = [sessionUID, weather, trackTemperature, airTemperature]
    print('sessionData: ', sessionData)

def GetCarSetup(packet):
    myCar = packet.carSetups[playerCarId]
    frontWing = myCar.frontWing
    rearWing = myCar.rearWing
    ballast = myCar.ballast
    fuelLoad = myCar.fuelLoad
    brakePressure = myCar.brakePressure
    brakeBias = myCar.brakeBias
    carSetupData = [frontWing, rearWing, ballast, fuelLoad, brakePressure, brakeBias]
    print('Setup: ', carSetupData)

def GetCarStatus(packet):
    myCar = packet.carStatusData[playerCarId]
    fuelMix = myCar.fuelMix
    fuelInTank = myCar.fuelInTank
    tyresWear = myCar.tyresWear # array di 4 elementi
    actualTyreCompound = myCar.actualTyreCompound
    tyresAgeLaps = myCar.tyresAgeLaps
    carStatusData = [fuelMix, fuelInTank, tyresWear, actualTyreCompound, tyresAgeLaps]
    print('carStatus: ', carStatusData)
    """
    with open('MLPython/Lap_project/Lap_time.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerow(data)
    """
def GetLapData(packet):
    myCar = packet.lapData[playerCarId]
    lastLapTime = myCar.lastLapTime
    currentLapNum = myCar.currentLapNum
    lapData = [lastLapTime, currentLapNum]
    print('lapData: ', lapData)

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
