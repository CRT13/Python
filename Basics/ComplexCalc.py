""" A five-function (+,-,*,/,abs) complex-number calculator program"""
######################## IMPORT LIBRARIES #######################
import math
##################### CLASS INITIALIZATIONS #####################
class complexCalc:
       
	def __init__(self, re=0, im=0):
		self.re = re
		self.im = im
		
	def __add__(self, n):
		return complexCalc(self.re + n.re, self.im + n.im)

	def __sub__(self, n):
		return complexCalc(self.re - n.re, self.im - n.im)

	def __mul__(self, n):
		real = (self.re*n.re - self.im*n.im)
		imag = (self.re*n.im + self.im*n.re)
		return complexCalc(real, imag)

	def __div__(self, n):
		real = (self.re*n.re + self.im*n.im)/(n.re**2 + n.im**2)
		imag = (self.im*n.re - self.re*n.im)/(n.re**2 + n.im**2)
		return complexCalc(real, imag)

	def __abs__(self):
		return (math.sqrt(self.re**2 + self.im**2))

	def __str__(self):

		if (self.im == 0):
			return ("%.2f" %(self.re))
		elif (self.re == 0):
			return ("%.2fi" %(self.im))
		else:
			if (self.im > 0):
				return ("%.2f + %.2fi" %(self.re, self.im))
			elif (self.im < 0):
				return ("%.2f - %.2fi" %(self.re, -1*self.im))
#################################################################
########################## MAIN PROGRAM #########################
flag = True
while flag:
    print('==========================================')
    print('=============== ComplexCalc ==============')
    print('==========================================')
    print('=========== (A,B) = (x+iy,z+iw) ==========')
    print('==========================================')
    re_1 = float(input('Re(A): '))
    im_1 = float(input('Im(A): '))
    re_2 = float(input('Re(B): '))
    im_2 = float(input('Im(B): '))
    print('==========================================')
    #Initialize instances of class
    x = complexCalc(re_1, im_1)
    y = complexCalc(re_2, im_2)
    #Run class methods
    add = x + y
    print ('A+B =',add)
    sub = x - y
    print ('A-B =',sub)
    mul = x * y
    print ('AxB =',mul)
    div = x.__div__(y)
    print ('A/B =',div)
    modx = x.__abs__()
    print ('|A| = %.2f'%(modx))
    mody = y.__abs__()
    print ('|B| = %.2f'%(mody))
    
    flag = int(input('Continue?(1/0)'))
#################################################################
