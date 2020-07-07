def first_negative(values):
    for v in values:
        if v<0:
            return v
            
# If an empty list is passed to this function, it returns `None`:

my_list = []
print(first_negative(my_list)
            