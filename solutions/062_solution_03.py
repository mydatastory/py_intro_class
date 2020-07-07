# We need to specify the path to the file of interest in the call to 
# `cudf.read_csv`. We first need to `jump` out of the folder `thesis` using
# `../` and then into the folder `field_data` using `field_data/`. Then we 
# can specify the filename `microbes.csv`.
#
# The result is as follows:

data_microbes = cudf.read_csv('../field_data/microbes.csv')