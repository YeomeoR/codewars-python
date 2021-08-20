# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
# Task Overview:
# You have to write a function that accepts three parameters:
# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
# Usage Examples:
# cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
# cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting

def enough(cap, on, wait):
    free_seats = cap - on
    getting_on = free_seats - wait
    waiting = abs(getting_on)
    return waiting if getting_on < 0 else 0


# def enough(cap, on, wait):
#   # free seats on the bus less the people at the stop waiting to get on
#     free_seats = cap - on
#     getting_on = free_seats - wait
# #   # if the result of 'getting on' is negative, that number will have to wait 
#     waiting = abs(getting_on)
    
#     if (getting_on < 0):
#         return waiting
#     elif (getting_on > 0):
#         return 0
# #     # all spaces are taken
#     else:
# #   # else if the number is above 0, all waiting can board the bus, no one waiting
#         return 0
    


print(enough(10, 5, 5), 0)
print(enough(100, 60, 50), 10)
print(enough(20, 5, 5), 0)