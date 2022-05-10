import csv

header = ['sessionUID','trackName','sessionType','weather','trackTemperaure','airTemperature', # sessionData
'frontWing', 'rearWing', 'onThrottle', 'offThrottle', 'frontCamber', 'rearCamber', 'frontToe', 'rearToe', 'frontSuspension',
'rearSuspension', 'frontAntiRollBar', 'rearAntiRollBar', 'frontSuspensionHeight', 'rearSuspensionHeight', 'rearLeftTyrePressure', 'rearRightTyrePressure',
'frontLeftTyrePressure', 'frontRightTyrePressure', 'ballast', 'brakePressure', 'brakeBias', # carSetup
'fuelMix', 'fuelInTank', 'tyresWear', 'tyreCompound', 'tyresAgeLaps', # carStatus
'lastLapTime', 'currentLapNum' # lapData
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
    return lapData

def cleanData(data):
    for lap in data:
        lap[1] = track[lap[1]]
        lap[2] = sessionType[lap[2]]
        lap[3] = weather[lap[3]]
        lap[27] = fuelMix[lap[27]]
        lap[30] = tyreCompound[lap[30]]
    return data

def writeData(lapData):
    with open('MLPython/Lap_project/Readable_lap_time.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerows(lapData)

data = getData()
readableData = cleanData(data)
writeData(readableData)