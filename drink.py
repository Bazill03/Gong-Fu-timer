#!/usr/bin/env python

import time
import sys
from argparse import ArgumentParser
from playsound import playsound

class CustomTea:
    "Allows the user to construct a custom tea"
    def __init__(self,name):
        self.name = name

#variables
#bool for max steeps
maxSteepBool = False
#number of steeps
steepCount = "1"
#max number of steeps
maxSteep = 0

#arguments
parser = ArgumentParser()
parser.add_argument("-c", "--custom", help="create custom timer")
parser.add_argument("-t", "--tea", help="Starts the program with preset parameters.")
parser.add_argument("-ib", "--initial", help="Sets the initial brew time for a custom tea.")
parser.add_argument("-bi", "--interval", help="Sets the interval for subsequent infustions.")
parser.add_argument("-ms", "--maxsteep", help="Sets a max number of steeps and will notify the user once its been reached")

args = parser.parse_args()

def timer(countdown):
    while countdown > 0:
        print(countdown)
        time.sleep(1)
        countdown = countdown - 1


def drink(brewTime, brewInt):
    global steepCount
    global maxSteep
    if(steepCount == maxSteep+1 and maxSteepBool == True):
        print("You've reached your max steeps. Hope you had a great session 😊!")
        exit()
    else:
        #change the brew time and the steep count to strings
        brewTime = str(brewTime)
        steepCount = str(steepCount)
        #Output for what steep and the amount of time for the steep
        print("...Brewing steep " + steepCount + " for " + brewTime + " seconds...")
        #changes variables back to integers
        brewTime = int(brewTime)
        steepCount = int(steepCount)
        brewInt = int(brewInt)
        #timer
        timer(brewTime)
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
        drink(brewTime, brewInt)
    return

if args.tea and args.initial and args.interval and args.maxsteep:
    #tea
    tea = args.tea
    tea = CustomTea(tea)
    print("Drinking " + tea.name)
    #inital brew
    tea.int_brew = args.initial
    intBrewtime = tea.int_brew
    print("Initial brew will be: " + tea.int_brew + " seconds.")
    #brew interval
    tea.brew_int = args.interval
    brewInt = args.interval
    print("Brew interval will be: " + tea.brew_int + " seconds.")
    #max steep
    tea.max_steep = args.maxsteep
    maxSteepBool = True
    maxSteep = tea.max_steep
    maxSteep = int(maxSteep)
    print("You will be enjoying " + tea.name + " for " + tea.max_steep + " steeps.")
    #waits for user to begin timer
    input("Press ENTER to begin infusion...")
    drink(tea.int_brew, tea.brew_int)

if args.tea and args.initial and args.interval:
    #tea
    tea = args.tea
    tea = CustomTea(tea)
    print("Drinking " + tea.name)
    #inital brew
    tea.int_brew = args.initial
    intBrewtime = tea.int_brew
    print("Initial brew will be: " + tea.int_brew + " seconds.")
    #brew interval
    tea.brew_int = args.interval
    brewInt = args.interval
    print("Brew interval will be: " + tea.brew_int + " seconds.")
    #waits for user to begin timer
    input("Press ENTER to begin infusion...")
    drink(tea.int_brew, tea.brew_int)


#Allows the user to set a custom timer
if args.custom:
    custom = args.custom
    print("Custom timer started for " + custom + " seconds.")
    custom = int(custom)
    timer(custom)
    #plays a friendly notification letting the user know the timer is complete
    playsound("notification.wav")
    print("Your custom timer is finished.")
    #exits the program
    exit()

#variables
#Gets users initial brewing time and converts it to int
intBrewTime = int(input("Enter initial brewing time: "))
#gets users brewing interval
brewInt = int(input("Enter brewing interval: "))
#asks the user if they want to set a max number of steeps
maxSteepConfirm = input("Would you like to set a max number of steeps? y/n: ")


if(maxSteepConfirm is "y" or "n"):
    if(maxSteepConfirm is "y"):
        maxSteepBool = True
        maxSteep = int(input("How many steeps?: "))
    elif(maxSteepConfirm is "n"):
        maxSteepBool = False
elif(maxSteepConfirm != "y" or "n"):
    print("Please enter y/n")
    maxSteepConfirm = input("Would you like to set a max number of steeps? y/n: ")



drink(intBrewTime)
