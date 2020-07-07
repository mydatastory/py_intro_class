# 1. ---------------------------------------------
year = 1983
gdp_decade = 'gdpPercap_' + str(year // 10)
avg = (japan.loc[gdp_decade + '2'] + japan.loc[gdp_decade + '7']) / 2

# 2. ---------------------------------------------
def avg_gdp_in_decade(country, continent, year):
    df = pandas.read_csv('data/gapminder_gdp_' + continent + '.csv', index_col=0)
    c = df.loc[country]
    gdp_decade = 'gdpPercap_' + str(year // 10)
    avg = (c.loc[gdp_decade + '2'] + c.loc[gdp_decade + '7'])/2
    return avg
    
# 3. --------------------------------------------
def avg_gdp_in_decade(country, continent, year): 
    df = pandas.read_csv(‘data/gapminder_gdp_’ + continent + ‘.csv’, index_col=0) 
    c = df.loc[country] 
    gdp_decade = ‘gdpPercap_’ + str(year // 10) 
    total = 0.0 num_years = 0 for yr_header in c.index
    total = total + c.loc[yr_header] num_years = num_years + 1 
    return total/num_years
    
