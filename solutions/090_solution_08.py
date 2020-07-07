# Program A ---------------------------------
#
# new is ['D', 'o', 'l', 'd'] and old is ['D', 'o', 'l', 'd']
#
# Program B ---------------------------------
# 
# new is ['D', 'o', 'l', 'd'] and old is ['g', 'o', 'l', 'd']
# 
# `new = old` makes `new` a reference to the list `old`; `new` and `old` point
# towards the same object.
#
# `new = old[:]` however creates a new list object `new` containing all elements
# from the list `old`; `new` and `old` are different objects.