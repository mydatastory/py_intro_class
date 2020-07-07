# The program prints `m`.
# 1. Python interprets a negative index as starting from the end (as opposed to
#    starting from the beginning).  The last element is `-1`.
# 2. The last index that can safely be used with a list of N elements is element 
#    `-N`, which represents the first element.
# 3. `del values[-1]` removes the last element from the list.
# 4. `values[:-1]`