# Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.
# Assume that the input n will always be a positive integer.
# Examples:
# sum_cubes(2)
# > 9 
# # sum of the cubes of 1 and 2 is 1 + 8

### from cs50 video python, lecture 2

# def sum_cubes(n):
#     cubed = []
#     i = 1
#     while (i <= n):
#         cubed.append(i**3)
#         i+=1
#     print(sum(cubed))

def sum_cubes(n):
    return sum(i**3 for i in range(0,n+1))
  
        

print(sum_cubes(1), 1)
print(sum_cubes(2), 9)
print(sum_cubes(3), 36)
print(sum_cubes(4), 100)
print(sum_cubes(10), 3025)
print(sum_cubes(123), 58155876)