#!/home/sahil/anaconda2/bin/python

#function to decompose the DNA strand 
def decompose(data):
	A=0			#initializing counts
	T=0
	C=0
	G=0	
	Other=0
	l=len(data)      
	for i in range(11,l-2):		#starting from 11 till l (because the actual characters are preceded by word "Decompose")
		if data[i] in ['A','a']:
			A = A+1
	
		elif data[i] in ['T','t']:
			T = T+1
					
		elif data[i]in ['C','c']:
			C = C+1
				
		elif data[i]in ['G','g']:
			G = G+1
			
		else :
			Other=Other+1
			print "WARNING: Found illegal character '",data[i],"' at position",i-11			
	print "{'A':%i, 'C':%i, 'T':%i, 'G':%i, 'Other':%i}" %(A,C,T,G,Other)
	

s = raw_input('Console Activated- Enter Command \n')   #input the string to be decomposed in the format - decompose("XXXXXXXXX") where X is the DNA Strand
decompose(s)  #calling decompose function, passing command line input 's'

