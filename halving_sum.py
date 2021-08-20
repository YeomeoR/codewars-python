# Given a positive integer n, calculate the following sum:
# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.
# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47
import math

def halving_sum(n): 
    the_list_to_be_summed = []
    # while n halved > 1
    while n >= 1:
    # put n into a list
        the_list_to_be_summed.append(n)
        n = math.floor(n / 2)
    # put n / 2 into a list
        # the_list_to_be_summed.append(n)
    # sum the elements in the created list
    return sum(the_list_to_be_summed)

# def halving_sum(n):
#     halved_list = []
#     halved_list.append(n)
#     for ele in halved_list:
#         if halved_list[-1] > 1:
#             halved_list.append(math.floor(ele/2))
#     print(sum(halved_list))
# halving_sum(25)
# halving_sum(127)
    

print(halving_sum(25),47)
print(halving_sum(127),247)