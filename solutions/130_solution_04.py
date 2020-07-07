import pandas

def min_in_data(filename):
    data = pandas.read_csv(filename)
    return data.min()