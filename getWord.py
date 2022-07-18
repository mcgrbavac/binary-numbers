#!/usr/bin/python3

answer_1 = input("In order for this script to run, you must have a word list file saved in this same directory. Continue (y/n)? ").strip().lower()
if answer_1 == "y":
	answer_2 = input("What is the name of the file? ").strip()
	with open(answer_2) as reader:
		wordList = reader.readlines()
	numberOfWords = len(wordList) - 1
#	numberOfWords = int(numberOfWords) - 1
	from conversionFunctions import *
	answer_3 = input("Would like to input a binary number (y/n)? ").strip().lower()
	if answer_3 == "y":
		y = decimal_to_binary(numberOfWords)
		stringPrint = "Input a binary number between 0 and {}: ".format(y)
		x = input(stringPrint).strip()
		z = binary_to_decimal(x)
		z = int(z)
		if z > numberOfWords or z < 0:
			print("You did not - " + stringPrint)
		else:
			output1 = wordList[z].strip()
			output2 = str(z)
			output3 =  x
			tableData = [[" ", "Word", "Decimal Number", "Binary Number"], ["1. ", output1, output2, output3]]
			for row in tableData:
				print("{: <4} {: <20} {: <20} {: <20}".format(*row))
	elif answer_3 == "n":
		answer_4 = input("Would you like to input a decimal number (y/n)? ").strip().lower()
		if answer_4 == "y":
			stringPrint = "Input a decimal number between 0 and {}: ".format(numberOfWords)
			z = input(stringPrint).strip()
			x = decimal_to_binary(z)
			z = int(z)
			if z > numberOfWords or z < 0:
				print("You did not - " + stringPrint)
			else:
				output1 = wordList[z].strip()
				output2 = str(z)
				output3 = x
				tableData = [[" ", "Word", "Decimal Number", "Binary Number"], ["1. ", output1, output2, output3]]
				for row in tableData:
					print("{: <4} {: <20} {: <20} {: <20}".format(*row))
		else:
			print("Goodbye.")
	else:
		print("Goodbye")
else:
	print("Please save a word list file in this directory.")

