#!/usr/bin/python3
import math
from conversionFunctions import *

def max_binary(x):
	y = math.log(2)
	r = math.log(x)
	z = r / y
	q = (2**math.ceil(z)) - x
	return(q)

def input_binary_length_check(x, y):
	x_length = len(x)
	y_length = len(y)
	if x_length <= y_length:
		return(y_length - x_length)
	elif x_length % y_length == 0:
		return(0)
	else:
		z = y_length - (x_length % y_length)
		return(z)


with open("list.txt") as reader:
	wordList = reader.readlines()
numberOfWords = len(wordList)
#Confirm max word number is a max binary number
wordCountCheck = max_binary(numberOfWords)
if wordCountCheck == 0:
	#get word count in binary and the length of binary
	numberOfWordsBinary = decimal_to_binary(numberOfWords-1)
	numberOfWordsBinaryLength = len(numberOfWordsBinary)
	#continue
else:
	nextClosestWordList = numberOfWords + wordCountCheck
	nextClosestWordListBinary = decimal_to_binary(nextClosestWordList)
	print("There are {} words in the list. Add {} words to match max binary number ({} or {}).".format(numberOfWords, wordCountCheck, nextClosestWordList, nextClosestWordListBinary))
	exit()

#Get input binary
inputBinary = input("Input your binary derived with entropy: ").strip()
inputDecimal = binary_to_decimal(inputBinary)
inputBinaryCheck = input_binary_length_check(inputBinary, numberOfWordsBinary)
if inputBinaryCheck == 0:
	#get number of words in our word list
	numOfWordsExtract = len(inputBinary) // len(numberOfWordsBinary)
	#continue
else:
	print("Your binary input is missing {} bits.".format(inputBinaryCheck))
	exit()

#Checksum the input binary
answer = input("Do you want to checksum the input binary? (y/n) ").strip().lower()
if answer == "y":
	checksum_Output = checksum_255(inputBinary)
	checksum_Boolean = checksum_Output[0]
else:
	checksum_Boolean = True
if checksum_Boolean == False:
	if checksum_Output[3] == "":
		print("Input binary is too short for an 8 bit checksum.")
		exit()
	else:
		print("Error with the checksum.")
		#This next print message uses a min of 8 characters in 2 of the variable input. This 8 is specific to the checksum_255 output since this checksum will output 8 bits.
		print("The following binary {0:0>b} has a checksum of {2:0>8b} which is different from the input of {1:0>8b}.".format(int(checksum_Output[1],2), int(checksum_Output[2],2), int(checksum_Output[3],2)))
		exit()
elif answer == "n":
	print("Did not check checksum. \n")
else:
	print("Good checksum. \n")

#Make an array of binary numbers
n = numberOfWordsBinaryLength
binaryArray = [inputBinary[i:i+n] for i in range(0, len(inputBinary), n)]

#Make an array of decimal numbers
decimalArray = [binary_to_decimal(binaryArray[i]) for i in range(0, numOfWordsExtract)]

#Make an array of words
wordArray = [wordList[decimalArray[i]].strip() for i in range(0, numOfWordsExtract)]

#Append the data tables
counter = 0
tableData = [[" ", "Word", "Decimal Number", "Binary Number"]]
for i in range(0, numOfWordsExtract):
	counter = counter + 1
	strCounter = str(counter) + ". "
	tableData.append([strCounter, wordArray[i], decimalArray[i], binaryArray[i]])
#Print the data table
for row in tableData:
	print("{: <4} {: <20} {: <20} {: <}".format(*row))

