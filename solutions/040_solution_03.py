# `max` and `min` return TypeErrors in the case because the correct number of 
# parameters was not supplied. If it just returned `None`, the error would be 
# much harder to trace as it would likely be stored into a variable and used 
# later in the program, only to likely throw a runtime error. 