#Author: Lara Floegel-Shettty
#Date: 12/2/17

#Precondition: User inputs valid string (either Rock, Paper, or Scissors)
#Postcondition: Program displays results of the game, whether user won or not

import random
import time
import sys

options = ["rock", "paper", "scissors"] #computer's options
computer = random.choice(options) #randomly selects element 

def delay(string): #writes the strings on the same line with time delay in between
    sys.stdout.write(string)
    sys.stdout.flush()

#intro
print("		Welcome To")
time.sleep(0.5)
delay("	    ROCK ")
time.sleep(0.5)
delay("PAPER ")
time.sleep(0.5)
delay("SCISSORS\n")
print("\n")
time.sleep(0.5)

#username
name = raw_input("Enter name: ")

#instructions
print("\n")
print("Hello " + name + "!\n")
print("The rules are simple:")
print("""   You have three choices: Rock, Paper, or Scissors.
Rock beats Scissors, Scissors beats Paper, and Paper 
beats Rock. Your mission is to choose one to try to beat the 
Computer. Good Luck!\n 
	""") 

play = "y"

#game runs at least once, repeats itself if user wants to play again
while ((play == "y") or (play == "yes")):
	choice = raw_input("Rock, Paper, or Scissors?\n")
	choice = choice.lower() #sets user's input to all lower case 


	#shows if user inputs invalid entry, repeats until valid string is entered
	while (choice != "rock" and choice != "paper" and choice != "scissors"):
		print("Please only enter Rock, Paper, or Scissors.")
		choice = raw_input("Enter new choice:\n")
		choice = choice.lower()

	print("\n")
	print("Let the game begin!")
	print("  ROCK ")
	time.sleep(0.5)
	print("  PAPER ")
	time.sleep(0.5)
	print("  SCISSORS")
	time.sleep(0.5)
	print("  SHOOT!\n")


	#prints results of the game depending on user input  
	if choice == computer:
		print("It's a tie!\n")

	#case 1: rock
	if choice == "rock":
		if computer == "paper":
			print("Computer wins!\n")
		elif computer == "scissors":
			print("You win!\n")

	#case 2: paper
	if choice == "paper":
		if computer == "scissors":
			print("Computer wins!\n")
		elif computer == "rock":
			print("You win!\n")

	#case 3: scissors
	if choice == "scissors":
		if computer == "rock":
			print("Computer wins!\n")
		elif computer == "paper":
			print("You win!\n")

	#asks if user wants to play again
	play = raw_input("Do you want to play again? [y/n]\n")

	#if invalid entry, repeats until valid one is entered
	while ((play != "y" and play != "yes") and (play != "n" and play != "no")):
		print("Please enter either y or n")
		play = raw_input("Do you want to play again?\n")

#if user enters "n" or "no", game ends and string is printed
print("Thanks for playing!\n")





