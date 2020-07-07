values = [-2,1,65,78,-54,-24,100]
smallest, largest = None, None

for v in values:
    if smallest==None and largest==None:
        smallest, largest = v, v
    else:
        smallest = min(smallest, v)
        largest = max(largest, v)

print(smallest, largest)