#string is made of characters - letters[a-z,A-Z], digits[0-9], special characters like comma, period, semicolon
# characters are stored in ASCII format or Unicode format (UTF-8,56 UTF-16,UTF-32)
str1 , str2 = "Hello", "   World    "
num = 10

# Basic operations on string
print(f"Concatenation of {str1} and {str2} = {str1 + str2}")
print(f"Repetition of {str1} {num} times = {str1 * num}")

#Advanced Operations
print(f"Number of characters in {str1} are {len(str1)}")
print(f"Convert {str1} to uppercase {str1.upper()}")
print(f"Convert {str1} to lowercase {str1.lower()}")
#colons are only put to emphasize that spaces are stripped out
print(f"Strip out all border spaces in :{str2}: :{str2.strip()}:")
print(f"Replace all 'l' in {str1} with 'ab' : {str1.replace('l','ab')}")
print(f"Find where {str2} is present in {str1} are {str1.find(str2)}")
print(f"Find where {'He'} is present in {str1} are {str1.find('He')}")
print(f"Find where {'h'} is present in {str1} are {str1.find('h')}")