data_all = pandas.read_csv('../data/gapminder_all.csv', index_col='country')
data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
              s=data_all['pop_2007']/1e6)
              
# A good place to look is the documentation for the plot function - 
# help(data_all.plot).

# kind - As seen already this determines the kind of plot to be drawn.

# x and y - A column name or index that determines what data will be placed on 
# the x and y axes of the plot

# s - Details for this can be found in the documentation of plt.scatter. A 
# single number or one value for each data point. Determines the size of the 
# plotted points.