def middle(a, b, c):
    '''Return the middle value of three.
    Assumes the values can actually be compared.'''
    values = [a, b, c]
    values.sort()
    return values[1]
    