'''
Apple Simulator
By Kazat0

Version: 1.0
'''


#Imports
from os import system
import subprocess as sp


#Variables
apples = 0
money = 0.0
energy = 1
maxCollecting = 10
applePrice = 0.25
passiveIncome = 0.0
workers = 0
salesPersons = 0
baskets = 0


#Functions

#Clear Screen
def ClearScreen():
	cls = sp.call("cls", shell=True)

#Stats Setup
def PrintStats():
	global apples
	global money
	global energy
	global workers
	global salesPersons
	global baskets

	print(name + "'s Stats:  \n")
	print("Apples:", apples)
	print("Money: $", money)
	print("Energy:", energy)
	print("Baskets:", baskets)
	print("Sales Persons:", salesPersons)
	print("Workers:", workers)

#Collect Apples
def CollectApples():
	global apples
	global energy
	global maxCollecting

	input("\n" + "Press enter button to begin collecting apples... \n")
	ClearScreen()
	applesInput = int(input("\n" + "How many apples do you want to collect?: "))
	if applesInput <= maxCollecting:
		apples += applesInput
		energy -= 1
		print("\n" + "You collected", applesInput, "apples! \n")
		print("You used 1 energy doing so. \n")
		input("Press enter to begin selling apples... \n")
	else:
		print("\n" + "You can only collect up to", maxCollecting, "apples! \n")
		CollectApples()

#Sell Apples
def SellApples():
	global apples
	global money
	global passiveIncome

	ClearScreen()
	print("Time to sell those apples! \n")
	print("The current price you can sell apples for is: $", applePrice, "\n")
	sellAmount = int(input("How many apples do you want to sell?: "))
	if sellAmount <= apples:
		profit = sellAmount * applePrice
		money += profit
		money += passiveIncome
		apples -= sellAmount
		print("\n" + "You sold", sellAmount, "apples! \n")
		print("You made: $", profit, "dollars in profit! \n")
		if workers >= 1: print("You also made: $", passiveIncome, "from your workers! \n")
		input("Press enter to continue... \n")
	else:
		print("\n" + "You don't have that many apples! \n")
		input("Press enter to continue... \n")
		SellApples()

#Shop
def Shop():
	global money
	global maxCollecting
	global passiveIncome
	global applePrice
	global workers
	global salesPersons
	global baskets

	ClearScreen()
	input("Press enter to begin shopping... \n")
	print("Shop: \n")
	print("Your money: $", money, "\n")
	print("1. Basket: $5 (increases the max apples you can collect)")
	print("2. Sales Person: $10 (increases apple sell price)")
	print("3. Worker: $10 (workers will harvest and sell apples for you! Passive income baby!) \n")
	shopChoice = input("Pick a selection to buy (type 'n' for none): ")
	if shopChoice == "1" and money >= 5:
		money -= 5.0
		maxCollecting += 10
		baskets += 1
		print("\n" + "You bought a basket! You can now collect 10 more apples! \n")
		input("Press enter to continue... \n")
		Shop()
	elif shopChoice == "2" and money >= 10:
		money -= 10.0
		applePrice += 0.25
		salesPersons += 1
		print("\n" + "You hired a sales person! You can sell apples for $0.25 more! \n")
		input("Press enter to continue... \n")
		Shop()
	elif shopChoice == "3" and money >= 10:
		money -= 10
		passiveIncome += 1.0
		workers += 1
		print("\n" + "You hired a worker! He will sell $1 worth of apples per day! \n")
		input("Press enter to continue... \n")
		Shop()
	elif shopChoice == "n":
		print("\n" + "You decided to stop shopping for today. \n")
		input("Press enter to continue... \n")
	else:
		print("\n" + "That is not a selection or you don't have enough money!\n")
		input("Press enter to continue... \n")
		Shop()

#Rest
def Rest():
	global energy

	ClearScreen()
	print("It's been a long day at work, time to rest! \n")
	input("Press enter to rest... \n")
	energy += 1
	print("You rested and gain 1 energy! \n")
	input("Press enter to continue... \n")

#Next Day
def NextDay():
	ClearScreen()
	print("The next day... \n")
	input("Press enter to continue... \n")

#Victory Check
def VictoryCheck():
	global money

	if money >= 1000000.0:
		Victory()

#Victory
def Victory():
	ClearScreen()
	print("You obtained 1 million dollars just from selling apples, you are now an apple tycoon! \n")
	print("Congratulations, you won the game!!! \n")
	input("Press enter to end... \n")
	print(" ,--./,-.")
	print("/ #      \\")
	print("|        |")
	print("\\        /")
	print(" `._,._,'")
	print("\n")
	print("Art by Hayley Jane Wakenshaw")
	quit()

#Run Game Cycle
def RunGameCycle():
	global apples
	global money
	global energy

	while True:
		PrintStats()
		CollectApples()
		SellApples()
		Shop()
		Rest()
		NextDay()
		VictoryCheck()


#Start
colors = sp.call("color 4f", shell=True)
ClearScreen()
print("\n" + "Welcome to Apple Simulator! \n")
print("To win the game, obtain 1 million dollars and become an apple tycoon! \n")
name = input("What is your name?: ")
print("\n" + "Your name is: " + name, "\n")
input("Press enter to continue... \n")
ClearScreen()

#Game
RunGameCycle()