original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result   = []

for value in original:
    if value<0.0:
        result.append(0)
    else:
        result.append(1)
        
print(result)