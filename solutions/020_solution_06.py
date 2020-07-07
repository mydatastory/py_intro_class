# 1. thing[low:high] returns a slice from `low` to the value before `high`
# 2. thing[low:] returns a slice from `low` to the end of `thing`
# 3. thing[:high] returns a slice from the beginning of `thing` to the value 
#     before `high`
# 4. thing[:] returns all of `thing`
# 5. thing[number:negative-number] returns a slice from `number` to 
#    `negative-number` values from the end of `thing`
# 6. If a part of the slice is out of range, the operation does not fail. 
#    `atom_name[0:15]` gives the same result as `atom_name[0:]`.