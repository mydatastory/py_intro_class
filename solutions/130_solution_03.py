# 1. The first line of output (`1871/3/19`) is from the print function inside 
#   `print_date()`, while the second line is from the print function below the 
#    function call. All of the code inside `print_date()` is executed first, and
#    the program then "leaves" the function and executes the rest of the code.   
# 2. The problem with the example is that the function is defined *after* the 
#    call to the function is made. Python therefore doesn't understand the 
#    function call.