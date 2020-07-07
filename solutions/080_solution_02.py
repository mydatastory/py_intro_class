data_asia = pandas.read_csv('../data/gapminder_gdp_asia.csv', index_col='country')
data_asia.describe().T.plot(kind='scatter', x='min', y='max')

# No particular correlations can be seen between the minimum and maximum gdp 
# values year on year. It seems the fortunes of asian countries do not rise and 
# fall together.

data_asia = pandas.read_csv('../data/gapminder_gdp_asia.csv', index_col='country')
plt.style.use('default')
data_asia.max().plot()

# Seems the variability in this value is due to a sharp drop after 1972. Some 
# geopolitics at play perhaps? Given the dominance of oil producing countries, 
# maybe the Brent crude index would make an interesting comparison? Whilst 
# Myanmar consistently has the lowest gdp, the highest gdb nation has varied 
# more notably.