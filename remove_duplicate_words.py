# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# Output:
# 'alpha beta gamma delta'

def remove_duplicate_words(s):
    word = s.split(' ')
    print(word)
    
    

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
    #   , "alpha beta gamma delta")
print(remove_duplicate_words("my cat is my cat fat"))
    #   , "my cat is fat")
