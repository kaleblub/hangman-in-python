"""
predefined word list
	- extra step, make genre choices
get length of the word
display the spaces for each character
display either the hangman or just the number of tries 

"""

from hangmanArt import *
import random

ART = {
	7: empty(),
	6: head(),
	5: neck(),
	4: oneArm(),
	3: twoArms(),
	2: back(),
	1: oneLeg(),
	0: twoLegs(),
	"fail": gameOver(),
	"win": congratulations()
}

LIVES = 7

wordNumber = random.randint(0, 855)

wordChoice = ""

with open("words.txt", "r") as words:
	wordChoice = words.readlines()[wordNumber - 1]

blanks = len(wordChoice) - 1

guesses = ["___"] * blanks

all_guesses = []


print(ART[LIVES], "\n", "___ " * blanks)



while True:

	if LIVES == 0:
		print(ART["fail"])
		False
		break
	elif LIVES > 0 and blanks == 0:
		print(ART["win"])
		False
		break

	chosenLetter = input("\nWhat letter do you choose?  ")

	if chosenLetter in wordChoice:
		print("\n\n\n\n\n\n\n____________________________\n\n\tCORRECT!")
		guesses[wordChoice.find(chosenLetter)] = chosenLetter
		all_guesses.append(chosenLetter)
		blanks -= 1
	else:
		print("\n\n\n\n\n\n\n____________________________\n\n\tINCORRECT!")
		LIVES -= 1
		all_guesses.append(chosenLetter)
		print("\nYOU HAVE", LIVES, "LIVES LEFT...")

	print(ART[LIVES], "\n")
	print(" ".join(guesses))
	print("\nYou have already chosen: ", " ".join(all_guesses))