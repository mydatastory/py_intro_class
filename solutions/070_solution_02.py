# No, they do not produce the same output! The output of the first statement is:

        gdpPercap_1952  gdpPercap_1957
country                                
Albania     1601.056136     1942.284244
Austria     6137.076492     8842.598030

# The second statement gives:

        gdpPercap_1952  gdpPercap_1957  gdpPercap_1962
country                                                
Albania     1601.056136     1942.284244     2312.888958
Austria     6137.076492     8842.598030    10750.721110
Belgium     8343.105127     9714.960623    10991.206760

# Clearly, the second statement produces an additional column and an additional 
# row compared to the first statement.  What conclusion can we draw? We see that 
# a numerical slice, 0:2, omits the final index (i.e. index 2) in the range 
# provided, while a named slice, gdpPercap_1952 : gdpPercap_1962 , includes 
# the final element.