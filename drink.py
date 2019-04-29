import time
import sys

#variables
#Gets users initial brewing time and converts it to int
intBrewTime = int(input("Enter initial brewing time: "))
#gets users brewing interval
brewInt = int(input("Enter brewing interval: "))
#asks the user if they want to set a max number of steeps
maxSteepConfirm = input("Would you like to set a max number of steeps? y/n: ")
#bool for max steeps
maxSteepBool = False
#number of steeps
steepCount = "1"

if(maxSteepConfirm == "y"):
    maxSteepBool = True
    maxSteep = int(input("How many steeps?: "))


def drink(brewTime):
    global steepCount
    if(steepCount == maxSteep+1 and maxSteepBool == True):
        print("You've reached your max steeps. Hope you had a great session 😊!")
    else:
        #change the brew time and the steep count to strings
        brewTime = str(brewTime)
        steepCount = str(steepCount)
        #Output for what steep and the amount of time for the steep
        print("...Brewing steep " + steepCount + " for " + brewTime + " seconds...")
        #changes variables back to integers
        brewTime = int(brewTime)
        steepCount = int(steepCount)
        #timer
        time.sleep(brewTime)
        #lets the user know they need to pour
        print("Finished!")
        #Adds the brew interval to total brew time
        brewTime = brewTime + brewInt
        #Changes the steep count
        steepCount = steepCount + 1
        #asks the user if ready for next steep
        confirm = input("Ready to go again? y/n:")
        #if the user is ready for the next steep, calls the timer
        if(confirm == "y"):
            drink(brewTime)
        else:
            #or exits the program
            exit()
    return


#waits for user to begin timer
input("Press enter to start steeping...")
drink(intBrewTime)
