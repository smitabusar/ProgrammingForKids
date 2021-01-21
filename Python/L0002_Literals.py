import sys
# Strings are characters enclosed in double or single quotes
print ("Any characters enclosed in double or single quotes is considered string in python")
print ('I am also a string')

#Print integers or float
print (5)
print (-5)
print (5.5)

#print special number values
print (sys.maxsize) #max int value which is power(2,63)-1
print (sys.float_info.max) #max float value
print (sys.float_info.min) #min float value
print (sys.float_info.epsilon) #1.0 - least value greater than 1.0 that is representable as a difference

#Print booleans which have the value True or False
print(True)
print(False)