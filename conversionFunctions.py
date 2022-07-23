#!/usr/bin/python3

import hashlib

def decimal_to_binary(x):
	x = int(x)
	if x == 0:
		return("0")
	elif x < 0:
		print("You must input a positive decimal number.")
	else:
		total = 0
		exponent = 0
		data = []
		while total <= x:
			total = 2**exponent
			if total > x:
				data.append(exponent)
				x = x - 2**(exponent - 1)
				total = 0
				exponent = 0
			else:
				exponent = exponent + 1
		numberString = ""
		for i in range(max(*data), 0, -1):
			if i in data:
				numberString = numberString + "1"
			else:
				numberString = numberString + "0"
		return(numberString)


def binary_to_decimal(x):
	if int(max(x))>1 or int(min(x))<0:
		print("Must input a binary number.")
	else:
		counter = len(x)
		storagevalue = 0 
		for i in x:
			y = int(i)
			value = y*(2**(counter-1))
			counter = counter - 1
			storagevalue = storagevalue + value
		return(storagevalue)

def hexadecimal_to_decimal(x):
	hexaTable = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
	deciTable = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	x_length = len(x)
	x_exponent = x_length - 1
	x_decimal = 0
	for i in range(0, x_length):
		for j in range(0, len(hexaTable)):
			if x[i] == hexaTable[j]:
				x_decimal = x_decimal + (deciTable[j] * 16**x_exponent)
		x_exponent = x_exponent - 1
	return(x_decimal)

def hexadecimal_to_binary(x):
	y = hexadecimal_to_decimal(x)
	z = decimal_to_binary(y)
	return(z)

def checksum_255(x):
	x = int(x)
	x_string = str(x)
	totalChecksumBits = 8
	totalHexidecimalLength = 2
	if x <= totalChecksumBits:
		return(False)
	else:
		x_length = len(x_string)
		x_start = x_length - totalChecksumBits
		x_checksumBits = x_string[x_start:x_length]
		x_inputBits = x_string[0:x_start]
		x_inputBits_Bits = x_inputBits.encode('utf-8')
		hashed_input = hashlib.sha256(x_inputBits_Bits).hexdigest()
		hashed_input_front = hashed_input[0:totalHexidecimalLength]
		hashed_input_front_binary = hexadecimal_to_binary(hashed_input_front)
		if x_checksumBits == hashed_input_front_binary:
			return(True)
		else:
			return(False)
