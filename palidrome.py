# is 's' a palindrome

# def is_palindrome(s):
#     palindrome = True if s.lower() == s[::-1].lower else False
#     return palindrome

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


print(is_palindrome('a'), True)
print(is_palindrome('aba'), True)
print(is_palindrome('Abba'), True)
print(is_palindrome('malam'), True)
print(is_palindrome('malaman'), False)