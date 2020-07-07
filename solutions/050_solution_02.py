# The [random module](randommod) seems like it could help you.

# The string has 11 characters, each having a positional index from 0 to 10. You 
# could use `random.randrange` function (or the alias `random.randint`
# if you find that easier to remember) to get a random integer between 0 and
# 10, and then pick out the character at that position:

from random import randrange
random_index = randrange(len(bases))
print(bases[random_index])

# or more compactly:

from random import randrange
print(bases[randrange(len(bases))])

# Perhaps you found the `random.sample` function? It allows for slightly 
# less typing:

from random import sample
print(sample(bases, 1)[0])

# Note that this function returns a list of values. We will learn about lists 
# in episode 11.

# There's also other functions you could use, but with more convoluted code as 
# a result.