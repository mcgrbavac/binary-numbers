#!/usr/bin/python3

answer = input("Do you want to convert a decimal number to a binary number? (y/n) ").strip().lower()
if answer == "y":
	answer_2 = input("Input a decimal number: ").strip()
	from conversionFunctions import decimal_to_binary
	y = decimal_to_binary(answer_2)
	print(y)
elif answer == "n":
	answer = input("Do you want to convert a binary number to a decimal number? (y/n) ").strip().lower()
	if answer == "y":
		answer_2 = input("Input a binary number: ").strip()
		from conversionFunctions import binary_to_decimal
		y = binary_to_decimal(answer_2)
		print(y)
	else:
		print("Goodbye.")
else:
	print("Goodbye.")
