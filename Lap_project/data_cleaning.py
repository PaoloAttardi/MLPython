import csv

header = ['sessionUID','trackName','sessionType','weather','trackTemperaure','airTemperature', # sessionData
'fuelMix', 'fuelInTank', 'tyresWear', 'tyreCompound', 'tyresAgeLaps', # carStatus
'lastLapTime', 'currentLapNum', 'position', 'setUpName' # lapData
]

headerSetUp = ['trackName', 'frontWing', 'rearWing', 'onThrottle', 'offThrottle', 'frontCamber', 'rearCamber', 'frontToe', 'rearToe', 'frontSuspension',
'rearSuspension', 'frontAntiRollBar', 'rearAntiRollBar', 'frontSuspensionHeight', 'rearSuspensionHeight', 'rearLeftTyrePressure', 'rearRightTyrePressure',
'frontLeftTyrePressure', 'frontRightTyrePressure', 'ballast', 'brakePressure', 'brakeBias', 'setUpName'
]

track = {
    '0': 'Melbourne',
    '1': 'Paul Ricard',
    '2': 'Shanghai',
    '3': 'Bahrain',
    '4': 'Catalunya',
    '5': 'Monaco',
    '6': 'Montreal',
    '7': 'Silverstone',
    '8': 'Hockenheim',
    '9': 'Hungaroring',
    '10': 'Spa',
    '11': 'Monza',
    '12': 'Singapore',
    '13': 'Suzuka',
    '14': 'Abu Dhabi',
    '15': 'Texas',
    '16': 'Brazil',
    '17': 'Austria',
    '18': 'Sochi',
    '19': 'Mexico',
    '20': 'Baku',
    '21': 'Sakhir Short',
    '22': 'Silverstone Short',
    '23': 'Texas Short',
    '24': 'Suzuka Short',
    '25': 'Hanoi',
    '26': 'Zandvoort'
    }

sessionType = {
    '0': 'unknown', '1': 'FP1', '2': 'FP2', '3': 'FP3', '4': 'ShortP', '5': 'Q1',
    '6': 'Q2', '7': 'Q3', '8': 'Short Q', '9': 'One Shot Q', '10': 'Race', '11': 'Race2',
    '12': 'Time Trial'
}

weather = {
    '0': 'clear', '1': 'light cloud', '2': 'overcast',
    '3': 'light rain', '4': 'heavy rain', '5': 'storm'
}

tyreCompound = {
    '16': 'C5', '17' : 'C4', '18' : 'C3', '19' : 'C2', '20' : 'C1',
    '7' : 'inter', '8' : 'wet',
    '9' : 'dry', '10' : 'wet',
    '11' : 'super soft', '12' : 'soft', '13' : 'medium', '14' : 'hard',
    '15' : 'wet'
}

fuelMix = {
    '0': 'lean', '1': 'standard', '2': 'rich', '3': 'max'
}

def getData():
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
    return lapData[0]

def getReadableData():
    allData = []
    with open('MLPython/Lap_project/Readable_lap_time.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                allData.append(row)
                line_count += 1
            else:
                line_count += 1
    return allData

def getSetUp():
    allSetUp = []
    with open('MLPython/Lap_project/Set_up.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                allSetUp.append(row)
                line_count += 1
            else:
                line_count += 1
    return allSetUp

def newSetUp(trackSetUp, usedSetUp):
    if trackSetUp == []:
        num = '100'
    else:
        lastSetUp = trackSetUp[len(trackSetUp) - 1]
        nameLastSetUp = lastSetUp[len(lastSetUp) - 1]
        usedSetUp[0].append(nameLastSetUp)
        check =  all(item in trackSetUp for item in usedSetUp) # controllare se l'ordine track/used è corretto
        if check is False:
            usedSetUp[0].pop()
            num = int(nameLastSetUp[-3:])  + 1
        else:
            return nameLastSetUp,False
    return usedSetUp[0][0] + str(num),True

def writeSetUp(data):
    with open('MLPython/Lap_project/Set_up.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headerSetUp)

        # write the data
        writer.writerows(data)

def cleanData(data):
    data[1] = track[data[1]]
    data[2] = sessionType[data[2]]
    data[3] = weather[data[3]]
    data[27] = fuelMix[data[27]]
    data[30] = tyreCompound[data[30]]
    return data

def writeData(lapData):
    toWrite = getReadableData()
    with open('MLPython/Lap_project/Readable_lap_time.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        toWrite.append(lapData[0:6] + lapData[27:35])
        writer.writerows(toWrite)

def main():
    data = getData()
    readableData = cleanData(data)

    allSetUp = getSetUp()
    trackSetUp = []
    usedSetUp = []
    usedSetUp.append(readableData[6:27])
    usedSetUp[0].insert(0,readableData[1])
    for item in allSetUp:
        if(readableData[1] == item[0]):
            trackSetUp.append(item)
    setUpName,new = newSetUp(trackSetUp, usedSetUp)
    readableData.append(setUpName)
    usedSetUp[0].append(setUpName)
    allSetUp.append(usedSetUp[0])
    if new is True:
        writeSetUp(allSetUp)
    writeData(readableData)
    open('MLPython/Lap_project/Lap_time.csv', 'w').close()