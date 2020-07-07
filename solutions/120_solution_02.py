import glob
import pandas

fewest = float('Inf')

for filename in glob.glob('data/*.csv'):
    dataframe = pandas.read_csv(filename)
    fewest = min(fewest, dataframe.shape[0]
    
print('smallest file has', fewest, 'records')