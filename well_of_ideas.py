# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

def well(x):
    good = x.count("good")
    return "I smell a series!" if good > 2 else "Publish!" if good else "Fail!"
    # good = 0
    # bad = 0
    # for ele in x:
    #     if ele == 'good':
    #         good += 1
    #     "elif ele == 'bad':"
    #         bad += 1

    # if good > 2:
    #     return "I smell a series!"
    # elif good > 0 and good < 3:
    #     return "Publish!"
    # else:
    #     return "Fail!"
    
 


print(well(['bad', 'bad', 'bad']), 'Fail!')
print(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')