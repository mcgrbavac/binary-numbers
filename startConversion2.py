#!/usr/bin/python3

def decimal_to_binary(x):
	y = "{0:0>1b}".format(int(x))
	return(y)

def binary_to_decimal(x):
	y = "{0:0>1}".format(int(x, 2))
	return(y)

def hexadecimal_to_decimal(x):
	y = "{0:0>1}".format(int(x, 16))
	return(y)

def hexadecimal_to_binary(x):
	y = "{0:0>1b}".format(int(x, 16))
	return(y)

def decimal_to_hexadecimal(x):
	y = "{0:0>1X}".format(int(x))
	return(y)

def binary_to_hexadecimal(x):
	y = "{0:0>1X}".format(int(x, 2))
	return(y)

#Initiation strings
stringInit = "Input the number associated with the action you would like to perform: \n"
stringDB = "1) Decimal to binary \n"
stringBD = "2) Binary to decimal \n"
stringHD = "3) Hexadecimal to decimal \n"
stringHB = "4) Hexadecimal to binary \n"
stringDH = "5) Decimal to hexadecimal \n"
stringBH = "6) Binary to hexadecimal \n"
stringEnd = "0) End me. \n"
fullStringInit = stringInit + stringDB + stringBD + stringHD + stringHB + stringDH + stringBH + stringEnd

#Number input strings
stringD = "decimal"
stringB = "binary"
stringH = "hexadecimal"
stringInput = "Input the {} number: "

#Input loop
answerInit = None
while answerInit != 0:
	answerInit = int(input(fullStringInit).strip())
	if answerInit == 1:
		fullStringInput = stringInput.format(stringD)
		answerInput = input(fullStringInput)
		y = decimal_to_binary(answerInput)
		print(y + "\n")
	elif answerInit == 2:
		fullStringInput = stringInput.format(stringB)
		answerInput = input(fullStringInput)
		y = binary_to_decimal(answerInput)
		print(y + "\n")
	elif answerInit == 3:
		fullStringInput = stringInput.format(stringH)
		answerInput = input(fullStringInput)
		y = hexadecimal_to_decimal(answerInput)
		print(y + "\n")
	elif answerInit == 4:
		fullStringInput = stringInput.format(stringH)
		answerInput = input(fullStringInput)
		y = hexadecimal_to_binary(answerInput)
		print(y + "\n")
	elif answerInit == 5:
		fullStringInput = stringInput.format(stringD)
		answerInput = input(fullStringInput)
		y = decimal_to_hexadecimal(answerInput)
		print(y + "\n")
	elif answerInit == 6:
		fullStringInput = stringInput.format(stringB)
		answerInput = input(fullStringInput)
		y = binary_to_hexadecimal(answerInput)
		print(y + "\n")
	elif answerInit == 0:
		print("Goodbye.")
	else:
		continue

exit()
