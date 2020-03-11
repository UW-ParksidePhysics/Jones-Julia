a = [1, 3, 5, 7, 11] # List
b = [13, 17] # List
c = a + b # New list from list addition
print (c) # Print list c
b[0] = -1 # CHanges the first element of b to -1
d = [e+1 for e in a] # Creates a new list from a + 1
print (d) # Prints list d
d.append(b[0] + 1) # Adds element 1 for b + 1 to d
d.append(b[-1] + 1) # Adds the last element of b + 1 to d
print (d[-2:]) # Prints the second to element of list d
for e1 in a:
    for e2 in b:
        print (e1 + e2) # Nesting arguement