#!/usr/bin/env python           
  
import time
import sys
from argparse import ArgumentParser
from playsound import playsound

#playspace
parser = ArgumentParser()
parser.add_argument("-c", "--custom", help="create custom timer")
parser.add_argument("-t", "--tea", help="Starts the program with preset parameters. Not currently working")
parser.add_argument("-e", "--enter", help="Enter in a custom tea. Start with --tea")
args = parser.parse_args()

if args.custom:
    custom = args.custom
    print("Custom timer started for " + custom + " seconds.")
    custom = int(custom)
    while custom > 0:
        print(custom)
        time.sleep(1)
        custom = custom - 1
    playsound("notification.wav")
    print("Your custom timer is finished.")
    exit()

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
#max number of steeps
maxSteep = 0

if(maxSteepConfirm is "y" or "n"):
    if(maxSteepConfirm is "y"):
        maxSteepBool = True
        maxSteep = int(input("How many steeps?: "))
    elif(maxSteepConfirm is "n"): 
        maxSteepBool = False
elif(maxSteepConfirm != "y" or "n"): 
    print("Please enter y/n")
    maxSteepConfirm = input("Would you like to set a max number of steeps? y/n: ")


def drink(brewTime):
    global steepCount
    global maxSteep
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
        brewCounter = brewTime
        while brewCounter > 0:
            print(brewCounter)
            time.sleep(1)
            brewCounter = brewCounter - 1
        #lets the user know they need to pour
        print("Finished!")
        #friendly notification that the user needs to pour
        playsound('notification.wav')
        #Adds the brew interval to total brew time
        brewTime = brewTime + brewInt
        #Changes the steep count
        steepCount = steepCount + 1
        #asks the user if ready for next steep
        confirm = input("Press ENTER to begin your next infusion...")
        #if the user is ready for the next steep, calls the timer
        drink(brewTime)
    return


#waits for user to begin timer
input("Press ENTER to begin infusion...")
drink(intBrewTime)
