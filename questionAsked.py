def confirmData():
    print("The list which is supposed to be printed. ")
    unarmedRaceList= []
    bodyCameraList= []
    mentalIllnessList= []

    with open('fatal-police-shootings-data.csv', 'r') as file:
        header = file.readline().strip().split(',')
    
        raceOnly = header.index('race')
        armedWith = header.index('armed_with')
        bodyCamera = header.index('body_camera')
        mentalIllness = header.index('was_mental_illness_related')

        for line in file:
            data = line.strip().split(',')

            if data[armedWith] == 'unarmed':
                unarmedRaceList.append(data[raceOnly])

            bodyCameraList.append(data[bodyCamera])

            mentalIllnessList.append(data[mentalIllness])

        for i in range(len(unarmedRaceList)):
            print("Unarmed Race List:", unarmedRaceList[i])  
            print("Body Camera List:", bodyCameraList[i])
            print("Mental Illness List:", mentalIllnessList[i])