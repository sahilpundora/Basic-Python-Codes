#!/home/sahil/anaconda2/bin/python

import sys  				#We need to import sys to read lines in the for loop

def processText(data):
	i=0 				#Initializing i to be used in while loop
	mystr=""			#Creating empty string to feed the output to
	while(i<len(data)-1):		#We use len-1 because file has an extra character in the end, which is null


		#For the format \uXXXX
		if data[i]== '\\' and data[i+1]=='u':
			#We commpare if the next four items after\u are Hexadecimal or not. If yes, only then we replace them.
			if data[i+2] in "0123456789ABCDEFabcdef" and data[i+3] in "0123456789ABCDEFabcdef" and data[i+4] in "0123456789ABCDEFabcdef" and data[i+5] in "0123456789ABCDEFabcdef" :
				mystr=mystr+data[i+6]		#Save the character in the new string (skipping \uXXXX - 5 Positions, hence selecting 6th)
				i = i+7 			#To skip position eliminating \uXXXX
			else :					#If \uXXXX where X!=Hexadecimal, then we do not replace the string and just move to next element to check	
				mystr=mystr+data[i]
				i=i+1
		elif data[i]== '\\' and data[i+1]=='x':
			if data[i+2] in "0123456789ABCDEFabcdef" and data[i+3] in "0123456789ABCDEFabcdef" :
				mystr=mystr+data[i+4]		#Save the character in the new string (skipping \uXX - 3 Positions, hence selecting 4th)
				i=i+5				#To skip position eliminating \uXX
			else :	
				mystr=mystr+data[i]		
				i=i+1
		else :
			mystr=mystr+data[i]
			i=i+1


	#Finally we print out the filtered text
	print mystr  


for line in sys.stdin.readlines():
	processText(line) 
			

