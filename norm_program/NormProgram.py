#NormProgram by Derrick Rocha.
#Started on 8/25/2014.


#import math module to use power function.
import math

#Returns a float that represents the p-norm of list v and power p.
def normP(power,vector):
	num = 0
	#calculates (v0)^p+(v1)^p+(vn)^p.
	for vect in vector:
		num+=math.pow(vect,power)
	#Determins p-norm by raising power to 1.0/power.	
	norm = math.pow(num,1.0/power)
	return norm

#Returns a float that represents the norm of list v.
def norm(vector):
	num2 = 0
	#calculates (v0)^p+(v1)^p+(vn)^p
	for vect in vector:
		num2+=math.pow(vect,2)
	#Determins norm by raising to 1.0/2.	
	norm2 = math.sqrt(num2)
	return norm2

	
#Returns a list from the data entered by the user.
def getVectors():
	vectors = list()
        done = False
        while not done:
                num = input("Enter element in vector. Press -1 when finished.:\n")
                if num == -1:
                        done  = True
                else:
                        vectors.append(num)
                        print str(num)+ " Entered in list!\n"
	return vectors

#Retrieves a list from getVectors,retrieves a power from 
#the user, then calls norm(power,vector) and prints the output.
def pNormSelected():
	vect = getVectors()
	pow = input("Enter the power.\n")
	magnatude = normP(pow,vect)
        print "The p-norm of the vector with power "+str(pow)+" is "+str(magnatude)

#Retrieves a list from getVectors, then calls norm(vector) and prints the output.
def ecluNormSelected():
	vect2 = getVectors();
	magnatude2 = norm(vect2)
	print "The norm of the vector entered is " + str(magnatude2)
	
#Displays main menu and loads choice
def printMenu():
	option = input("\nWelcome to Norm Program!\n------------------"+
	"----------------------------------------------------\n1)-Press"+
	" 1 for p-norm function.\n2)-Press 2 for eucludian norm function\n");

	if option == 1:
		pNormSelected()
	elif option == 2:
		ecluNormSelected()
	else:
		print "You must enter either a 1 or a 2."

printMenu()
