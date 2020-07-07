calling <function report at 0x7fd128ff1bf8> 22.5

# A function call always needs parenthesis, otherwise you get memory address of 
# the function object. So, if we wanted to call the function named report, and 
# give it the value 22.5 to report on, we could have our function call as 
# follows:

print("calling")
report(22.5)