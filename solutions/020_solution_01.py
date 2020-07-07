# Command  # Value of x   # Value of y   # Value of swap #
x = 1.0    # 1.0          # not defined  # not defined   #
y = 3.0    # 1.0          # 3.0          # not defined   #
swap = x   # 1.0          # 3.0          # 1.0           #
x = y      # 3.0          # 3.0          # 1.0           #
y = swap   # 3.0          # 1.0          # 1.0           #

# These three lines exchange the values in `x` and `y` using the `swap`
# Variable for temporary storage. This is a fairly common programming idiom.