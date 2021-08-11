# Given an array of terms, if any of those terms relate to Alan Partridge, return Mine's a Pint!

# The number of ! after the t should be determined by the number of Alan related terms you find in the provided array (x). The related terms are:

# Partridge
# PearTree
# Chat
# Dan
# Toblerone
# Lynn
# AlphaPapa
# Nomad

# If you don't find any related terms, return 'Lynn, I've pierced my foot on a spike!!'

def part(arr):
    alpha_papa_isms = ['Partridge','PearTree','Chat','Dan','Toblerone','Lynn','AlphaPapa','Nomad']
    counter = 0
    for ele in arr:
        if ele in alpha_papa_isms:
            counter += 1
        
    return "Mine's a Pint" + ("!" * counter) if counter >= 1 else "Lynn, I've pierced my foot on a spike!!"
    
        







print(part(["Grouse", "Partridge", "Pheasant"]), "Mine's a Pint!")
print(part(["Pheasant", "Goose", "Starling", "Robin"]), "Lynn, I've pierced my foot on a spike!!")
print(part(["Grouse", "Partridge", "Partridge", "Partridge", "Pheasant"]), "Mine's a Pint!!!")
print(part([]), "Lynn, I've pierced my foot on a spike!!")
print(part(["Grouse", "Partridge", "Pheasant", "Goose", "Starling", "Robin", "Thrush", "Emu", "PearTree", "Chat", "Dan", "Square", "Toblerone", "Lynn", "AlphaPapa", "BMW", "Graham", "Tool", "Nomad", "Finger", "Hamster"]), "Mine's a Pint!!!!!!!!")