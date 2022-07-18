#!/usr/bin/python3

def decimal_to_binary(x):
	x = int(x)
	if x == 0:
		print("0")
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


