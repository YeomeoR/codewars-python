# use intersect to work out who got the most correct lottery numbers and print out a sentence with the details

lottery_numbers = {1,4,5,3,8}
player1 = {'name':'Roberto', 'numbers': {1,2,3,4,5}}
player2 = {'name':'Lex', 'numbers': {4,2,8,7,9}}


p1_matched = lottery_numbers.intersection(player1['numbers'])
p1_how_many = len(p1_matched)

p2_matched = lottery_numbers.intersection(player2['numbers'])
p2_how_many = len(p2_matched)

print(f'Player 1 matched {p1_how_many}  with these numbers: {p1_matched}. Player 2 matched {p2_how_many} with these numbers: {p2_matched}.')