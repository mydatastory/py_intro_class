from math import degrees, pi
angle = degrees(pi / 2)
print(angle)

# Most likely you find this version easier to read since it's less dense.
# The main reason not to use this form of import is to avoid name clashes.
# For instance, you wouldn't import `degrees` this way if you also wanted to 
# use the name `degrees` for a variable or function of your own. Or if you 
# were to also import a function named `degrees` from another library. 