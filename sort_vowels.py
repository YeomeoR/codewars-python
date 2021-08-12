# Sort the Vowels!
# In this kata, we want to sort the vowels in a special format.

# Task
# Write a function which takes a input string s and return a string in the following way:

   
#                   C|                          R|
#                   |O                          n|
#                   D|                          d|
#    "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
#                   W|                          T|
#                   |A                          |e
#                   R|                          5|
#                   S|                          T|

# Notes:

# List all the Vowels on the right side of |
# List every character except Vowels on the left side of |
# Return every character in its original case
# Each line is seperated with \n
# Invalid input ( undefined / null / integer ) should return an empty string


def sort_vowels(s):
    if s == None or s == "" or s == int:
        raise Exception("The arguments 'string' is None or empty")
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    s_listed = list(s)
    stringed = ''
    for character in s:
        if character in vowels:
            stringed += "|" + character + "\n"
        else:
            stringed += character + "|\n"
    stringed = stringed[:-1]
    return(stringed)
    
         
    
    

print(sort_vowels('Codewars'))
# , 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|')
print(sort_vowels('Rnd Te5T'))
    #   , 'R|\nn|\nd|\n |\nT|\n|e\n5|\nT|') 
