# Create a function close_compare that accepts 3 parameters: a, b, and an optional margin. The function should return whether a is lower than, close to, or higher than b.
# a is considered "close to" b if margin is greater than or equal to the distance between a and b.
# Please note the following:
# When a is close to b, return 0.
# Otherwise...
# When a is less than b, return -1.
# When a is greater than b, return 1.
# If margin is not given, treat it as zero.
# Assume: margin >= 0

def close_compare(a, b, margin):

    # if(not margin):
    #     return 0
    if margin >= (b - a):
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1
    elif not margin:
        return 0
        
    


# print(close_compare(4, 5), -1)
# print(close_compare(5, 5), 0)
# print(close_compare(6, 5), 1)
print(close_compare(2, 5, 3), 0)
print(close_compare(5, 5, 3), 0)
print(close_compare(8, 5, 3), 0)
print(close_compare(8.1, 5, 3), 1)
print(close_compare(1.99, 5, 3), -1)