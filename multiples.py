# Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3, "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5, and "Miss" if it isn't divisible by any of them. Note: Your program should only return one value

# Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom"


def multiple(x):
    return "BangBoom" if x%15==0 else "Boom" if x%5==0 else "Bang" if x%3==0 else "Miss"
    # if(x%15==0):
    #     return "BangBoom"
    # elif(x%5==0):
    #     return "Boom"
    # elif(x%3==0):
    #     return "Bang"
    # else:
    #     return "Miss"


print(multiple(30), "BangBoom")
print(multiple(3), "Bang")
print(multiple(98),"Miss")
print(multiple(65),"Boom")
print(multiple(23),"Miss")
print(multiple(15),"BangBoom")