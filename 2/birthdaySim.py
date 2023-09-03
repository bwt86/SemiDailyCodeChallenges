#Challenge is Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com

#import datetime and random libraries
import datetime, random

#todo: create functions to generate set of random birthdays given a number of birthdays to create 
def generateBirthdays(numberToGenerate):
    randomBirthdays = []
    #Generates random birthdays by adding a random number of days to the starting day of a year (as low as 0 days and as high as 364 days)
    for i in range(numberToGenerate):
        randDays   = random.randint(0, 364)
        randomBirthdays.append(datetime.date(2023,1,1)+ datetime.timedelta(days=randDays))
    return randomBirthdays 

#todo: create funtion to run 100000 simulations of birhtday generation
def runSimulations(simsToRun = 1, bDaysPerSim = 25):
    print(f'Generating a set of {bDaysPerSim} birthdays {simsToRun} times...')
    sims = []
    for i in range(simsToRun):
        sims.append(generateBirthdays(bDaysPerSim))
        #display progress
        if round(i/simsToRun, 6) == .1:
            print("10% Generated...")
        if round(i/simsToRun, 6) == .5:
            print("50% Generated...")
        if round(i/simsToRun, 6) == .9:
            print("90% Generated...")
        if round(i/simsToRun, 6) == 1:
            print("100% Generated...")
    return sims

#todo: create funtions to get statistics of simulation
def getSimStats(simData):
    print("Analyzing Simulations...")
    matchCount = 0
    for sim in simData:
        #checks if there is a match in a similation by seeing if the set is shorter than the list (sets can't have dupicates so if set is shorter then there was at least 1 matching birthday)
        if len(set(sim)) < len(sim):
            matchCount += 1
    print(f'Out of {len(simData)} sims run, there was a matching birthday {matchCount} times.\nThat means the percentage of the time matching birthdays occured in simulations of {len(sim)} people was {round((matchCount/len(simData)) * 100, 4)}%!') 

#main function
def main():
    numBDays = int(input('How many Birthdays should be generated per simulation?\n'))
    getSimStats(runSimulations(100000,numBDays))

# If the program is run, run the simuilation:
if __name__ == '__main__':
    main()