# Let P = a set of primary meals
# Let S = a set of sauces
# Let PR = a set of proteins
# Let PS = a set of possible combinations of primary and sauce
# Let FM = a set of items in the food menu

P = ["eba", "rice", "fufu", "yam", "bread", "plantain"]
S= ["egg", "stew", "afang", "egusi", "beans", "white soup", "pepper soup"]
PR=["chicken", "beef", "chevon", "pork", "fish"]
PS = []
FM = []

# For I in range(len(P)):
#     For J in range(len(S)):
#         Store P[I] + “"",”+ S[J] in PS
#     End loop
# End loop

for i in range(len(P)):
    for j in range(len(S)):
        PS.append(P[i]+", "+S[j])

# For I in range(len(PS)):
#     For J in range(len(R)):
#         Store PS[I] + “and”+ PR[J] in FM
#     End loop
# End loop

for i in range(len(PS)):
    for j in range(len(PR)):
        FM.append(PS[i]+" and "+PR[j])

# Display FM
for each in FM:
    print(each)