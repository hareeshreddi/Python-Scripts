a = list(map(int,input().split()))     # Input the list of numbers
d = {}                               # Start with empty dictionary
for x in a:
    if x not in d:                   # If this element occures first time
        d[x] = 1                     # Add new key to dictionary with value 1
    else:                            # If this element has already occured
        d[x] += 1                    # Increase count of this element

print(d)