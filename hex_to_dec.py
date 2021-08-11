# convert hex to decimal

def hex_to_dec(s):
    return int(s, 16)

print(hex_to_dec("1"), 1)
print(hex_to_dec("a"), 10)
print(hex_to_dec("10"), 16)