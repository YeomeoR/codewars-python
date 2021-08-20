# It involves implementing a program that sums the digits of a non-negative integer. For example, the sum of 3433 digits is 13.
# Digits can be a number or a string, and you should control it is no undefined and return an empty string.
# Digits can be a number or a string, and you should ensure it is not None and return an empty string.
# To give you a little more excitement, the program will not only write the result of the sum, but also write all the sums used: 3 + 4 + 3 + 3 = 13.

def sum_of_digits(digits): 
    for digit in digits:
        split_it = list(digits)
        int_list = [int(i) for i in split_it]
        added = sum(int_list)
        return added
    print(added)

print(sum_of_digits("3433"), "3 + 4 + 3 + 3 = 13")
print(sum_of_digits("64323"), "6 + 4 + 3 + 2 + 3 = 18")
print(sum_of_digits("8"), "8 = 8")