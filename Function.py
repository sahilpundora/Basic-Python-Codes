#!/home/sahil/anaconda2/bin/python

import sys
import matplotlib.pyplot as plt #for plotting
import numpy as np #to calculate array

#function for factorial
def factorial(fac):
    if fac > 1:
        return fac * factorial(fac - 1)
    else:
        return 1

#Function to calculate beta density points
def betafunction(a,b,val):
	fa=factorial(a-1.0)
	fb=factorial(b-1.0)
	fab=factorial(a+b-1.0)
	values=list()
	for i in range(0,len(val)):
			calculation= ( fab / (fa*fb) )*(val[i]**(a-1))*((1-val[i])**(b-1))
			values.append(calculation)
	return values

#function to plot the graph
def plot(x,X):
	plt.title('Beta Function Values')
	plt.grid=True
	p=plt.plot(x,X,lw=2,c='r')
	plt.xlabel('Values of x')
	plt.ylabel('Beta Density')
	plt.show()
	

#Input alpha,beta,x
alpha = float(raw_input('Enter Alpha: '))
beta = float(raw_input('Enter Beta: '))
print "Choose following option- 1 or 2"
print "1.Manually enter value(s) for x (single or multiple)"
print "2.Calculate Beta Density for X ranging from 0.000 to 0.999"
option=input("")
if option==1:
	number=input("How many X's you want to plot the Function for(number):")
	x=list()
	i=0
	#if x is more than one value, following is used to create a list of values for x
	while i < number:	
		print "Enter x no. %i" %(i+1)
		y= float(raw_input(''))
		x.append(y)
		i = i+1
elif option==2:
	x = np.arange(0.000,0.999,0.001)


#final values that are going to be used for generating the function
print ' '
print 'Beta function values will now be caluclated for the following-'
print 'Alpha=%f' %(alpha)
print 'Beta=%f' %(beta)
print 'x=',x
print ' '
print ' '



#Graph will be plotted between calculated values and values chosen for x
X=betafunction(alpha,beta,x)
print "Beta function will be now plotted for the following-"
print "Values of x:", x
print "Corresponding beta function values:", X
plot (x,X)









