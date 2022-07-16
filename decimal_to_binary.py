#!/usr/bin/python3

x = input("Input a decimal number: ").strip()
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
	data2 = []
	for i in range(max(*data), 0, -1):
		if i in data:
			data2.append(1)
		else:
			data2.append(0)
	print(*data2)
