#!/usr/bin/python3

answer = input("Do you want to convert a decimal number to a binary number? (y/n) ").strip().lower()
if answer == "y":
	from decimal_to_binary import *
	print("Hello")
elif answer == "n":
	answer = input("Do you want to convert a binary number to a decimal number? (y/n) ").strip().lower()
	if answer == "y":
		from binary_to_decimal import *

		print("Two")
	else:
		print("Goodbye.")
else:
	print("Goodbye.")
