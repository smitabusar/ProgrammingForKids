# Variable is place in memory whose value can be modified
# Variable names should letters, _ and digits. Should be in snake_case

# Read a string input with Prompt
name = input("Enter your name")

# Read a number - int or float
age = int(input("Enter Your age"))
weight = float(input("Enter Your weight"))

print(f'''
    Hello {name} !!
    You are {age} years old with weight is {weight: .2f} lbs.
    ''')