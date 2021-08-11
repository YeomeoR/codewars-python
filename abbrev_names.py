# abbreviate first and last names to jusdt the initials

def abbrev_name(name):
    uc = name.upper();
    split_names = uc.split()
    return split_names[0][0] + '.' + split_names[1][0]


print(abbrev_name("Sam harris"), "S.H")
print(abbrev_name("Patrick Feenan"), "P.F")
print(abbrev_name("Evan Cole"), "E.C")
print(abbrev_name("P Favuzzi"), "P.F")
print(abbrev_name("David Mendieta"), "D.M")