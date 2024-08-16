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

# List of expected races to filter valid data
    validRaces = ['W', 'B', 'A', 'H', 'O', 'N']

# Open the CSV file and process it
    with open('fatal-police-shootings-data.csv', 'r') as file:
        reader = csv.DictReader(file)
    
        for row in reader:
            race = row['race'].strip()  # Strip any whitespace
            armedStatus = row['armed_with']
        
        # Filter only valid race values
            if race in validRaces:
            # Count total occurrences of each race
                if race in raceCounts:
                    raceCounts[race] += 1
                else:
                    raceCounts[race] = 1
            
            # Count unarmed occurrences of each race
                if armedStatus == 'unarmed':
                    if race in unarmedRaceCounts:
                        unarmedRaceCounts[race] += 1
                    else:
                        unarmedRaceCounts[race] = 1

# Calculate the proportion of unarmed shootings by race
    unarmed_proportions = {}
    for race in raceCounts:
        unarmed_proportions[race] = (unarmedRaceCounts.get(race, 0) / raceCounts[race]) * 100

# Sort the data by race for a clean line plot
    sortedRaces = sorted(unarmed_proportions.keys())
    sortedPercentage = [unarmed_proportions[race] for race in sortedRaces]

# Visualization: Line graph
    plt.figure(figsize=(10, 6))
    plt.plot(sortedRaces, sortedPercentage, marker='o', color='blue')
    plt.title('Proportion of Unarmed Shootings by Race')
    plt.xlabel('Race')
    plt.ylabel('Percentage of Unarmed Shootings')
    plt.grid(True)
    plt.show()

def questionTwo():
    print("Question Two")

def questionThree():
    print("Question Three")


if __name__ == "__main__":
    main()