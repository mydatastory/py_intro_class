# It would be unreasonable to expect the Python in the command to convert the 
# string "3.4" to 3.4 and an additional type conversion to 3. After all, Python  
# performs a lot of other magic - isn't that part of its charm?
#
# However, Python throws an error. Why? To be consistent, possibly. If you ask 
# Python to perform two consecutive typecasts, you must convert it explicitly 
# in code, as in line 2 below.

int("3.4")
int(float("3.4"))