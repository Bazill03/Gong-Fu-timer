#!/usr/bin/env python

import time
import sys
from argparse import ArgumentParser
from playsound import playsound
import pickle

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
parser.add_argument("-nt","--newtea", help="runs the new tea utility with the name of the tea.")
parser.add_argument("-c", "--custom", help="create custom timer")
parser.add_argument("-t", "--tea", help="Starts the program with preset parameters.")
parser.add_argument("-ib", "--initial", help="Sets the initial brew time for a custom tea.")
parser.add_argument("-bi", "--interval", help="Sets the interval for subsequent infustions.")
parser.add_argument("-ms", "--maxsteep", help="Sets a max number of steeps and will notify the user once its been reached")

args = parser.parse_args()

#countdown function
def timer(countdown):
    while countdown > 0:
        print(countdown)
        time.sleep(1)
        countdown -= 1

def confirm():
    waiting = input("Please press ENTER to begin...")

#main function of the program
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
        brewTime += brewInt
        #Changes the steep count
        steepCount += 1
        #asks the user if ready for next steep
        confirm()
        #if the user is ready for the next steep, calls the timer
        drink(brewTime, brewInt)
    return

#This code runs if the user only specifies the -t tag
if args.newtea:
   print("Welcome to the custom tea wizard!")
   teaCreator_tea = args.newtea
   teaCreator_int_brew = input("Please enter the inital brew time in seconds: ")
   teaCreator_brew_int = input("Please enter the interval time in seconds: ")
   teaCreator_max_steep = input("Please enter the max steeps for this tea: ")
   teaDict = {1:teaCreator_tea,2:teaCreator_int_brew,3:teaCreator_brew_int,4:teaCreator_max_steep}
   pickle_out = open(teaCreator_tea + ".pickle","wb")
   pickle.dump(teaDict, pickle_out)

   print("===============")
   print("You've entered the tea name: " + teaDict[1])
   print("Inital steep for " + teaDict[1] + " will be " + teaDict[2] + " seconds.")
   print("Brew interval for " + teaDict[1] + " will be " + teaDict[3] + " seconds.")
   print(teaDict[1] + " will go for " + teaDict[4] + " rounds.")
   print("Please run the timer with -t " + teaDict[1] + ".")
   pickle_out.close()
   exit();

if args.tea:
    #this code runs if the user wants to begin a saved tea
    teaDict = str(args.tea + ".pickle")
    pickle_in = open(teaDict, "rb")
    teaPickle = pickle.load(pickle_in)
    print("You will be enjoying: " + teaPickle[1] + " for " + teaPickle[4] + " steeps. Enjoy! 😁")
    maxSteep = int(teaPickle[4])
    maxSteepBool = True
    confirm()
    drink(teaPickle[2],teaPickle[3])
    pickle_in.close()


#This code is run if the user uses all 4 arguments. Simply assgins the variables and runs the drink function.
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

#added this in case the user does not include a maxsteeps arguement
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

#If the user does not select any arguments, the program will run from here.

#variables
#Gets users initial brewing time and converts it to int
intBrewTime = int(input("Enter initial brewing time: "))
#gets users brewing interval
brewInt = int(input("Enter brewing interval: "))
#asks the user if they want to set a max number of steeps

while True:
    maxSteepConfirm = input("Would you like to set a max number of steeps? y/n: ")
    if maxSteepConfirm == "y":
        maxSteepBool = True
        maxSteep = int(input("How many steeps?: "))
        break
    elif maxSteepConfirm == "n":
        maxSteepBool = False
        break
    else:
        print("Please enter y/n")
        maxSteepConfirm = input("Would you like to set a max number of steeps? y/n: ")



drink(intBrewTime, brewInt)
