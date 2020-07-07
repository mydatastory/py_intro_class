# 1. Using the help(math) we see the we've got pow(x,y) in additon to sqrt(x)
# 2. The sqrt(x) fucntion (like much of the `math` library) has it's origins 
#    in C's math library. Consequently, it might be somewhat faster than pow(x,y). 
#    Also, it might be more readable than pow(x, 0.5) when implementing equations. 
#    However, sqrt(x) doesn't support negative arguments.