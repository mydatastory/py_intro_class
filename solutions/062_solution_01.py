# To read in a CSV, we use `pandas.read_csv`and pass the filename 
# 'data/gapminder_gdp_americas.csv' to it. We also once again pass the column 
# name 'country' to the parameter `index_col` in order to index by country: 

americas = cudf.read_csv('data/gapminder_gdp_americas.csv', index_col='country')