import glob
import pandas 
import matplotlib.pyplot as plt 

fig, ax = plt.subplots(1,1)

for filename in glob.glob('data/gapminder_gdp*.csv'):
    dataframe = pandas.read_csv(filename)
    # extract region from the filename, expected to be in the format 'data/gapminder_gdp_<region>.csv'
    region = filename.rpartition('_')[2][:-4] 
    dataframe.mean().plot(ax=ax, label=region)
    
plt.legend()
plt.show()