'''

-------------------COMMENT HEADER-------------------
Questions:
1. Is there a correlation between the race of individuals and the likelihood of being shot while unarmed?
2. Does the presence of a body camera reduce the likelihood of fatal shootings?
3. How much does the presence of mental illness in a suspect influence the probability of police shootings?

'''
import csv
import statistics as stats
import matplotlib.pyplot as plt

def main():
    # confirmData() this is the function to be called for printing the lists. 
    questionAsked()

# function for printing out the relevant lists. 
# def confirmData():
#     print("The list which is supposed to be printed. ")
#     unarmedRaceList= []
#     bodyCameraList= []
#     mentalIllnessList= []

#     with open('fatal-police-shootings-data.csv', 'r') as file:
#         header = file.readline().strip().split(',')
    
#         raceOnly = header.index('race')
#         armedWith = header.index('armed_with')
#         bodyCamera = header.index('body_camera')
#         mentalIllness = header.index('was_mental_illness_related')

#         for line in file:
#             data = line.strip().split(',')

#             if data[armedWith] == 'unarmed':
#                 unarmedRaceList.append(data[raceOnly])

#             bodyCameraList.append(data[bodyCamera])

#             mentalIllnessList.append(data[mentalIllness])

#         for i in range(len(unarmedRaceList)):
#             print("Unarmed Race List:", unarmedRaceList[i])  
#             print("Body Camera List:", bodyCameraList[i])
#             print("Mental Illness List:", mentalIllnessList[i])


def questionAsked():
    print('''
    
    These are the list of questions that you can ask:\n
    1. Is there a correlation between the race of individuals and the likelihood of being shot while unarmed?
    2. Does the presence of a body camera reduce the likelihood of fatal shootings?
    3. How much does the presence of mental illness in a suspect influence the probability of police shootings?''')

    questionNumber=int(input("Enter which question you would like to ask: "))

    if (questionNumber > 0 and questionNumber < 4):
        
        if (questionNumber == 1):
            questionOne()
        elif(questionNumber == 2):
            questionTwo()
        else:
            questionThree()
    else:
        print("\n")
        print("Enter valid question number")
        questionAsked()

    

def questionOne():
    raceCounts = {}
    unarmedRaceCounts = {}

    # Only the list of races which is in the data stored in an array which is also the x-axis of our visualization
    validRaces = ['W', 'B', 'A', 'H', 'O', 'N']


    with open('fatal-police-shootings-data.csv', 'r') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            race = row['race'].strip()  
            armedStatus = row['armed_with']
        
            if race in validRaces:
            # Total Occurences for all the races including armed and non armed data.
                if race in raceCounts:
                    raceCounts[race] += 1
                else:
                    raceCounts[race] = 1
            
            # Now if the person of that race was unarmed then the count is increased or introduced to the list. 
                if armedStatus == 'unarmed':
                    if race in unarmedRaceCounts:
                        unarmedRaceCounts[race] += 1
                    else:
                        unarmedRaceCounts[race] = 1

    # code to calculate the percentage of unarmed shootings according to the race
    unarmed_proportions = {}
    for race in raceCounts:
        unarmed_proportions[race] = (unarmedRaceCounts.get(race, 0) / raceCounts[race]) * 100

    #cleaning the data by sorting it
    sortedRaces = sorted(unarmed_proportions.keys())
    sortedPercentage = [unarmed_proportions[race] for race in sortedRaces]

    # visualizing the data through a line graph to show corelation
    plt.figure(figsize=(10, 6))
    plt.plot(sortedRaces, sortedPercentage, marker='o', color='blue')
    plt.title('Proportion of Unarmed Shootings by Race')
    plt.xlabel('Race')
    plt.ylabel('Percentage of Unarmed Shootings')
    plt.grid(True)
    plt.show()
    print("Total counts by race:", raceCounts)
    print("Unarmed counts by race:", unarmedRaceCounts)
    print("Unarmed proportions by race:", unarmed_proportions)






def questionTwo():
    
    totalShootings = 0
    cameraShootings = 0
    noCameraShootings = 0


    with open('fatal-police-shootings-data.csv', 'r') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            totalShootings += 1
        
        # Checking and increasing the counter by 1 every time a bodycam was used
            if row['body_camera'].lower() == 'true':
                cameraShootings += 1
            else:
                noCameraShootings += 1

    #calculating the percentage of shootings with camera and with no camera
    cameraShootingsProportion = (cameraShootings / totalShootings) * 100
    noCameraShootingsProportion = (noCameraShootings / totalShootings) * 100

    # the scope of the categories are limited so predefining it. 
    categories = ['With Body Camera', 'Without Body Camera']
    proportions = [cameraShootingsProportion, noCameraShootingsProportion]


    plt.figure(figsize=(8, 5))
    plt.bar(categories, proportions, color=['green', 'red'], alpha=0.6)
    plt.title('Proportion of Fatal Shootings by Body Camera Usage')
    plt.xlabel('Body Camera Usage')
    plt.ylabel('Percentage of Fatal Shootings')
    plt.ylim(0, 100)
    plt.show()
    print(f"Percentage of Fatal Shootings With Body Camera: {cameraShootingsProportion:.2f}%")
    print(f"Percentage of Fatal Shootings Without Body Camera: {noCameraShootingsProportion:.2f}%")





def questionThree():
    
    totalShootings = 0
    mentalIllnessShootings = 0
    noMentalIllnessShootings = 0


    with open('fatal-police-shootings-data.csv', 'r') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            totalShootings += 1
        
        # increading the counter by one everytime a shooting with mental illness was reported
            if row['was_mental_illness_related'].lower() == 'true':
                mentalIllnessShootings += 1
            else:
                noMentalIllnessShootings += 1

    # Calculating the percentage of people with mental illness and without mental illness
    mentalIllnessProportion = (mentalIllnessShootings / totalShootings) * 100
    noMentalIllnessProportion = (noMentalIllnessShootings / totalShootings) * 100

    # predefining the scope of the data 
    labels = ['Mental Illness Reported', 'No Mental Illness Reported']
    proportions = [mentalIllnessProportion, noMentalIllnessProportion]
    colors = ['skyblue', 'lightcoral']

    plt.figure(figsize=(8, 8))
    plt.pie(proportions, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Police Shootings by Mental Illness Report')
    plt.show()

    # Using the statistics module to calculate the Variance and SD. 
    variance = stats.variance(proportions)
    std_deviation = stats.stdev(proportions)

    print(f"Mental Illness Reported: {mentalIllnessProportion:.2f}%")
    print(f"No Mental Illness Reported: {noMentalIllnessProportion:.2f}%")
    print(f"Variance of percentage: {variance:.2f}")
    print(f"Standard Deviation of percentage: {std_deviation:.2f}")



if __name__ == "__main__":
    main()