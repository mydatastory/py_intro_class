# 1. -------------------------------------
data['gdpPercap_1982']

# 2. -------------------------------------
data.loc['Denmark',:]

# 3. -------------------------------------
data.loc[:,'gdpPercap_1985':]

# Pandas is smart enough to recognize the number at the end of the column label 
# and does not give you an error, although no column named `gdpPercap_1985` 
# actually exists. This is useful if new columns are added to the CSV file later.

# 4. -------------------------------------
data['gdpPercap_2007']/data['gdpPercap_1952'] 
