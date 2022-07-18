#!/usr/bin/python3
import math

def max_binary(x):
	y = math.log(2)
	r = math.log(x+1)
	z = r / y
	q = (2**(math.ceil(z))-1) - x
	return(q)





with open("list.txt") as reader:
	wordList = reader.readlines()
numberOfWords = len(wordList)
#Confirm max word number is a max binary number
from conversionFunctions import *
wordCountCheck = max_binary(numberOfWords)
if wordCountCheck == 0:
	numberOfWordsBinary = decimal_to_binary(numberOfWords)
	numberOfWordsBinaryLength = len(numberOfWordsBinary)
	#Get input binary
	inputBinary = input("Input your binary: ").strip()
	inputDecimal = binary_to_decimal(inputBinary)
	
	
	print(inputBinary)
	print(len(inputBinary))
	print(inputDecimal)
else:
	nextClosestWordList = numberOfWords + wordCountCheck
	nextClosestWordListBinary = decimal_to_binary(nextClosestWordList)
	print("There are {} words in the list. Add {} words to match max binary number ({} or {}).".format(numberOfWords, wordCountCheck, nextClosestWordList, nextClosestWordListBinary))
