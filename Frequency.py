#!/home/sahil/anaconda2/bin/python

import sys #for reading lines
import optparse #for -f functionality
import matplotlib.pyplot as plt #for plotting

#Function to accumulate all the lines read by the sys.stdin.readlines()	
def makestring(data, chars):
	l=len(data)-1  #here we use len - 1 because the file has an extra character in the end, which is null
	chars = ""
	for i in range(0,l):
		chars = chars + data[i]
	return chars

#Function to calculate Frequency
def processText(Text,X, Y):					
	l=len(Text)
	frequency=0
	bstring=""
	for i in range(0,l):
		frequency=Text.count(Text[i])
		if Text[i] not in bstring :
			X.extend([Text[i]])
			Y.extend([frequency])		
			bstring = bstring+Text[i]			

#Function to plot the bar chart
def plot(X,Y):
	print X
	print Y
	plt.title('Character Frequency')
	plt.grid=True
	p=plt.bar(X,Y)
	plt.xlabel('Characters')
	plt.ylabel('Count')
	plt.show()
	


#Global Variable Declaration
Text =""
chars =""
X =['Characters']
Y =['Frequency']


#create a new option parser for -f functionality
parser = optparse.OptionParser()
parser.add_option('-f', '--file', dest='fileName', help='file name to read from')


#get the options entered by the user at the terminal
(options, others) = parser.parse_args()

#inspect the options entered by the user!
if options.fileName is None:
	print "DEBUG: the user did not enter the -f option"
	for line in sys.stdin.readlines():
		Text= Text + makestring(line, chars) #calling characters accumulating function
	processText(Text,X,Y) #calling character count(frequency) function, passing global variables X and Y
	X=X[1:] #Reassigning X starting from 1 position (removing word 'Characters')
	Y=Y[1:]	#Reassigning Y starting from 1 position (removing word 'Frequency')
	plot(X,Y) #Calling the Plot function, and passing X and Y for plotting

#same as above followed for -f functionality
else:
	print "DEBUG: the user entered the -f option"
	print "DEBUG: the file name entered was: ", options.fileName
	file = open(options.fileName, "r") 
	for line in file:
		Text= Text + makestring(line, chars) 
	processText(Text,X,Y)
	X=X[1:]
	Y=Y[1:]
	plot(X,Y)       

			
	

	
	

		



				

