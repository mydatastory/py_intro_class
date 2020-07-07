import glob
import pandas

for filename in glob.glob('data/*.csv'):
    contents = pandas.read_csv(filename)
    if len(contents)<50:
        print(filename, len(contents))