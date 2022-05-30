import socket
from time import sleep
import data_cleaning
import csv
import numpy as np
from threading import Thread
from f1_2020_telemetry.packets import unpack_udp_packet

header = ['sessionUID','trackId','sessionType','weather','trackTemperaure','airTemperature', # sessionData
'frontWing', 'rearWing', 'onThrottle', 'offThrottle', 'frontCamber', 'rearCamber', 'frontToe', 'rearToe', 'frontSuspension',
'rearSuspension', 'frontAntiRollBar', 'rearAntiRollBar', 'frontSuspensionHeight', 'rearSuspensionHeight', 'rearLeftTyrePressure', 'rearRightTyrePressure',
'frontLeftTyrePressure', 'frontRightTyrePressure', 'ballast', 'brakePressure', 'brakeBias', # carSetup
'fuelMix', 'fuelInTank', 'tyresWear', 'actualTyreCompound', 'tyresAgeLaps', # carStatus
'lastLapTime', 'currentLapNum', 'position' # lapData
]
playerCarId = None
lastLapNum = 1
data = ['sessionData','carSetup','carStatus','lapData']

def switch(packet_id, packet):
    if packet_id == 1:
        data[0] = GetSessionData(packet)
    elif packet_id == 2:
        GetLapData(packet)
    elif packet_id == 5:
        data[1] = GetCarSetup(packet)
    elif packet_id == 7:
        data[2] = GetCarStatus(packet)

def GetData():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)  
    UDP_PORT = 20777
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_socket.bind((IPAddr, UDP_PORT))
    while True:
        global stop_threads
        if stop_threads:
            break
        udp_packet = udp_socket.recv(2048)
        packet = unpack_udp_packet(udp_packet)
        header = packet.header
        global playerCarId
        playerCarId = header.playerCarIndex
        switch(header.packetId,packet)

def GetSessionData(packet):
    # packet = packet.PacketSessionData controlla come accedere al ai dati della sessione
    weather = packet.weather
    trackId = packet.trackId
    sessionType = packet.sessionType
    trackTemperature = packet.trackTemperature
    airTemperature = packet.airTemperature
    sessionUID = packet.header.sessionUID
    sessionData = [sessionUID, trackId, sessionType, weather, trackTemperature, airTemperature]
    return sessionData

def GetCarSetup(packet):
    myCar = packet.carSetups[playerCarId]
    frontWing = myCar.frontWing
    rearWing = myCar.rearWing
    onThrottle = myCar.onThrottle
    offThrottle = myCar.offThrottle
    frontCamber = myCar.frontCamber
    rearCamber = myCar.rearCamber
    frontToe = myCar.frontToe
    rearToe = myCar.rearToe
    frontSuspension = myCar.frontSuspension
    rearSuspension = myCar.rearSuspension
    frontAntiRollBar = myCar.frontAntiRollBar
    rearAntiRollBar = myCar.rearAntiRollBar
    frontSuspensionHeight = myCar.frontSuspensionHeight
    rearSuspensionHeight = myCar.rearSuspensionHeight
    rearLeftTyrePressure = myCar.rearLeftTyrePressure
    rearRightTyrePressure = myCar.rearRightTyrePressure
    frontLeftTyrePressure = myCar.frontLeftTyrePressure
    frontRightTyrePressure = myCar.frontRightTyrePressure
    ballast = myCar.ballast
    brakePressure = myCar.brakePressure
    brakeBias = myCar.brakeBias
    carSetupData = [frontWing, rearWing, onThrottle, offThrottle, frontCamber, rearCamber, frontToe, rearToe, frontSuspension,
    rearSuspension, frontAntiRollBar, rearAntiRollBar, frontSuspensionHeight, rearSuspensionHeight, rearLeftTyrePressure, rearRightTyrePressure,
    frontLeftTyrePressure, frontRightTyrePressure, ballast, brakePressure, brakeBias]
    return carSetupData

def GetCarStatus(packet):
    myCar = packet.carStatusData[playerCarId]
    fuelMix = myCar.fuelMix
    fuelInTank = myCar.fuelInTank
    tyresWear = myCar.tyresWear # array di 4 elementi
    tyresWear = np.sum(tyresWear)/4 # General Wear
    actualTyreCompound = myCar.actualTyreCompound
    tyresAgeLaps = myCar.tyresAgeLaps
    carStatusData = [fuelMix, fuelInTank, tyresWear, actualTyreCompound, tyresAgeLaps]
    return carStatusData

def GetLapData(packet):
    myCar = packet.lapData[playerCarId]
    lastLapTime = myCar.lastLapTime
    currentLapNum = myCar.currentLapNum
    carPosition = myCar.carPosition
    global lastLapNum
    if(currentLapNum > lastLapNum):
        sleep(1)
        global data
        lastLapNum = currentLapNum
        lapData = [lastLapTime, currentLapNum, carPosition]
        data[3] = lapData
        write_data_thread = Thread(target=WriteData,args=(data,))
        write_data_thread.start()

def WriteData(data):
    lapData = []
    with open('MLPython/Lap_project/Lap_time.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                lapData.append(row)
                line_count += 1
            else:
                line_count += 1
    if(data != None): lapData.append(data[0] + data[1] + data[2] + data[3])
    with open('MLPython/Lap_project/Lap_time.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerows(lapData)
    data_cleaning.main()

def userInput():
    print('Digita "n" per fermare la raccolta dati: ')
    input_check = input()
    if (input_check == 'n'):
        global stop_threads
        stop_threads = True
        hostname = socket.gethostname()    
        IPAddr = socket.gethostbyname(hostname)  
        UDP_PORT = 20777
        stop_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        stop_socket.sendto(b'hi', (IPAddr, UDP_PORT))

"""
The Thread() accepts many parameters. The main ones are:

target: specifies a function (GetData) to run in the new thread.
args: specifies the arguments of the function (GetData). The args argument is a tuple.

creo un nuovo thread per ricevere i dati
"""

stop_threads = False
get_data_thread = Thread(target=GetData)
stop_receive_data = Thread(target=userInput)
get_data_thread.start()
stop_receive_data.start()
stop_receive_data.join()
print('Fine raccolta dati')