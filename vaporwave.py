# Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence 
# converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this 
# V A P O R W A V E effect.
# Examples
# "Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
# "Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"

def vaporcode(s):
    # vaporised = [x for x in s if s.replace(" ","")]
    # return "  ".join(vaporised).upper()
    
#     trimmed = s.replace(" ","")
#     return "  ".join(trimmed).upper()

# def vaporcode(s):
    return "  ".join(s.replace(" ", "").upper())
        
        
    
    
print(vaporcode("Lets go to the movies"),"L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
print(vaporcode("Why isn't my code working?"),"W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")