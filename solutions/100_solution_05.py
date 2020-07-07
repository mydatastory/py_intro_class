sum = 0
data = [1,2,2,5]
cumulative = []

for number in data:
    sum += number
    cumulative.append(sum)
print(cumulative)