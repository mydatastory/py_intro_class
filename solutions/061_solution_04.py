# In order to write the DataFrame `americas` to a file called `processed.csv`, 
# execute the following command:

americas.to_csv('processed.csv')

# For help on `to_csv`, you could execute, for example,

help(americas.to_csv)

# Note that `help(to_csv)` throws an error! This is a subtlety and is due to 
# the fact that `to_csv` is NOT a function in and of itself and the actual 
# call is `americas.to_csv`. 