# Let's go through this piece of code line by line.

first = pandas.read_csv('data/gapminder_all.csv', index_col='country')

# This line loads the dataset containing the GDP data from all countries into a 
# dataframe called `first`. The `index_col='country'` parameter selects which 
# column to use as the row labels in the dataframe.  

second = first[first['continent'] == 'Americas']

# This line makes a selection: only those rows of `first` for which the 
# 'continent' column matches 'Americas' are extracted. Notice how the Boolean 
# expression inside the brackets, `first['continent'] == 'Americas'`, is used 
# to select only those rows where the expression is true. Try printing this 
# expression! Can you print also its individual True/False elements? (hint: 
# first assign the expression to a variable) 

third = second.drop('Puerto Rico')

# As the syntax suggests, this line drops the row from `second` where the label 
# is 'Puerto Rico'. The resulting dataframe `third` has one row less than the 
# original dataframe `second`.

fourth = third.drop('continent', axis = 1)

# Again we apply the drop function, but in this case we are dropping not a row 
# but a whole column. To accomplish this, we need to specify also the `axis` 
# parameter (we want to drop the second column which has index 1).

fourth.to_csv('result.csv')

# The final step is to write the data that we have been working on to a csv 
# file. Pandas makes this easy with the `to_csv()` function. The only required 
# argument to the function is the filename. Note that the file will be written 
# in the directory from which you started the Jupyter or Python session.
