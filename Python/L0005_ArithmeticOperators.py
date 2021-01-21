import math
# Basic operations
num1 , num2, f1 = 10, 4 , 53.45678
TWO = 2
#Python has no constant check. We create a sperate file and name Constants as UPPERCASE

# * , / , //, % has higher precedence than + , -
# 2 operators of same precendence than solve left to right
print(f"Sum of {num1} and {num2} = {num1 + num2}")
print(f"Product of {num1} and {num2} = {num1 * num2}")
print(f"Difference of {num1} and {num2} = {num1 - num2}")
print(f"Division of {num1} and {num2} = {num1 / num2}")
print(f"Quoitent and Remainder of {num1} and {num2} = {num1 // num2} R {num1 % num2}")


#Advanced Operations
print(f"{num1} squared = {num1 ** TWO}")
print(f"{num1} cubed = {math.pow(num1,3)}")
print(f"{num1} squareroot = {math.sqrt(num1)}")
print(f"PI is {math.pi:.4f}")
print(f"absolute of {-10}  = {math.fabs(-10)}")
print(f"maximum between {num1} and {num2}  = {max(num1,num2)}")
print(f"minimum between {num1} and {num2}  = {min(num1,num2)}")
print(f"truncate {f1}  = {math.trunc(f1)}")
print(f"floor of {f1}  = {math.floor(f1)}") # gives largest integer less than equal to number
print(f"ceil of {f1}  = {math.ceil(f1)}") # gives smallest integer greater than number