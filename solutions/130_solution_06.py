# 1. `2003/2/1`
# 2. We saw examples of using *named arguments* when working with the pandas 
#    library. For example, when reading in a dataset using 
#    `data = pandas.read_csv('data/gapminder_gdp_europe.csv', 
#    index_col='country')`, the last argument `index_col` is a named argument.  
# 3. Using named arguments can make code more readable since one can see from 
#    the function call what name the different arguments have inside the 
#    function. It can also reduce the chances of passing arguments in the wrong 
#    order, since by using named arguments the order doesn't matter.