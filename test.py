s = "h\te\tl\tl\to"
#expand_1 = s.replace("\t", " ")
#expand_2 = s.replace("\t", "  ")
#print(len(expand_1))
#print(len(expand_2))

ex_1 = s.expandtabs(1)
ex_2 = s.expandtabs(2)
print(ex_1, len(ex_1))
print(ex_2, len(ex_2))


