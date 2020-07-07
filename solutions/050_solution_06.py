# 1. Library calls 1 and 4. In order to directly refer to `sin` and `pi` 
#    without the library name as prefix, tyou need to use the `from 
#    ... import ...` statement. Whereas library call 4 imports all functions 
#    in the `math` module.
# 2. Library call 3. Here `sin` and `pi` are referred to with a shortened 
#    library name `m` instead of `math`. Library call 3 does exactly that using 
#    the `import ... as ...` syntax - it creates an alias for `math` in the 
#    form of the shortened name `m`.
# 3. Library call 2. Here `sin` and `pi` are referred to with the regular 
#    library name `math`, so the regular `import ...` call suffices.