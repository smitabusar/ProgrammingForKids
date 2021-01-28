# Print multiple lines using string enclosed in triple single or double quotes
print ('''
    Hello
    How are you
    ''')
#Print some special characters(Escape sequences) example like \t for tab, \' for single quote, \n for newline
print ("Hello\tWorld")
print (''' This is my teacher's book ''')

# print as a fraction
print ((.5).as_integer_ratio())
# print number in specified format 0W.P - represents the padded digit default is space, 10 represents total width, 3 represents digits after decimal
print (" % .3f" %5.5)
print (" %10.2f" %5.5)
print (" %10.3f" %345.55678)
print (" %010.3f" %345.55628)

#print a expression - string interpolation
print (f"Sum of {3} and {4} is \t {3+4}")
print (f"Sum of {3:5.2f} and {4.5:5.2f} is \t {3+4.5:5.2f}")