# Given a string, return a copy of the string with the vowels' case swapped.
# For this kata, assume that vowels are in the set "aeouiAEOUI".
# Example: Given a string "C is alive!", your function should return "C Is AlIvE!"
# Addendum: Your solution is only required to work for the ASCII character set.

# def swap_vowel_case(st): 
#     # lc = ['a','e','i','o','u']
#     # uc = ['A','E','I','O','U']
#     n = len(st)
#     str1 = ''
#     for i in range(n):
#         if (st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u'):
#             c = st[i].upper()
#             str1 += c
#         elif (st[i] == 'A' or st[i] == 'E' or st[i] == 'I' or st[i] == 'O' or st[i] == 'U'):
#             c = st[i].lower()
#             str1 += c
#         else:
#             str1 += st[i]
            
#     return str1

def swap_vowel_case(st): 
    vowels = 'aeouiAEOUI'
    for char in st: 
        if char in vowels: 
            st = st.replace(char, char.swapcase())
    return st
    


print(swap_vowel_case(" "), " ")
print(swap_vowel_case("C Is AlIvE!"), "C is alive!")
print(swap_vowel_case("to"), "tO")
print(swap_vowel_case("The"), "ThE")