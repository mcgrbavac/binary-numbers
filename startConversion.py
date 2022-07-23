#!/usr/bin/python3

from conversionFunctions import *

#Decimal to binary
answer = input("do you want to convert a decimal number to a binary number? (y/n) ").strip().lower()
if answer == "y":
	answer_2 = input("Input a decimal number: ").strip()
	y = decimal_to_binary(answer_2)
	print(y)
	exit()
elif answer == "n":
	answer = ""
else:
	print("Goodbye")
	exit()

#Binary to decimal
answer = input("Do you want to convert a binary number to a decimal number? (y/n) ").strip().lower()
if answer == "y":
	answer_2 = input("Input a binary number: ").strip()
	y = binary_to_decimal(answer_2)
	print(y)
	exit()
elif answer == "n":
	answer = ""
else:
	print("Goodbye")
	exit()

#Hexadecimal to decimal
answer = input("do you want to convert a hexadecimal number to decimal number? (y/n) ").strip().lower()
if answer == "y":
	answer_2 = input("Input a hexadecimal number: ").strip()
	y = hexadecimal_to_decimal(answer_2)
	print(y)
	exit()
elif answer == "n":
	answer = ""
else:
	print("Goodbye")
	exit()

#Hexadecimal to binary
answer = input("Do you want to convert a hexadecimal number to a binary number? (y/n) ").strip().lower()
if answer == "y":
	answer_2 = input("Input a hexadecimal number: ").strip()
	y = hexadecimal_to_binary(answer_2)
	print(y)
	exit()
elif answer == "n":
	answer = ""
	print("Goodbye")
	exit()
else:
	print("Goodbye")
	exit()
