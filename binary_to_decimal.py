#!/usr/bin/pthyon3

x = input("Input a binary number: ").strip()
if int(max(x))>1 or int(min(x))<0:
	print("Must input a binary number.")
else:
	counter = len(x)
	storagevalue = 0
	for i in x:
		y = int(i)
		value = y*(2**(counter -1))
		counter = counter - 1
		storagevalue = storagevalue + value
	print(storagevalue)

