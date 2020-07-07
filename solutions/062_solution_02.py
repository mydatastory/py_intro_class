# 1. We can check out the first five rows of `americas` by executing 
# `americas.head()` (allowing us to view the head of the DataFrame). We can 
# specify the number of rows we wish to see by specifying the parameter `n` 
# in our call to `americas.head()`. To view the first three rows, execute:

americas.head(n=3)

# The output is then

         continent  gdpPercap_1952  gdpPercap_1957  gdpPercap_1962  \
country                                                               
Argentina  Americas     5911.315053     6856.856212     7133.166023   
Bolivia    Americas     2677.326347     2127.686326     2180.972546   
Brazil     Americas     2108.944355     2487.365989     3336.585802`   

          gdpPercap_1967  gdpPercap_1972  gdpPercap_1977  gdpPercap_1982  \
country                                                                     
Argentina     8052.953021     9443.038526    10079.026740     8997.897412   
Bolivia       2586.886053     2980.331339     3548.097832     3156.510452   
Brazil        3429.864357     4985.711467     6660.118654     7030.835878`   

          gdpPercap_1987  gdpPercap_1992  gdpPercap_1997  gdpPercap_2002  \
country                                                                     
Argentina     9139.671389     9308.418710    10967.281950     8797.640716   
Bolivia       2753.691490     2961.699694     3326.143191     3413.262690   
Brazil        7807.095818     6950.283021     7957.980824     8131.212843`   

          gdpPercap_2007  
country                    
Argentina    12779.379640  
Bolivia       3822.137084  
Brazil        9065.800825

# 2. To check out the last three rows of `americas`, we would use the command, 
# `americas.tail(n=3)`, analogous to `head()` used above. However, here we want 
# to look at the last three columns so we need to change our view and then use 
# `tail()`. To do so, we create a new DataFrame in which rows and columns are 
# switched

americas_flipped = americas.T

# We can then view the last three columns of `americas` by viewing the last 
# three rows of `americas_flipped`:

americas_flipped.tail(n = 3)

# The output is then:

country        Argentina  Bolivia   Brazil   Canada    Chile Colombia  \
gdpPercap_1997   10967.3  3326.14  7957.98  28954.9  10118.1  6117.36   
gdpPercap_2002   8797.64  3413.26  8131.21    33329  10778.8  5755.26   
gdpPercap_2007   12779.4  3822.14   9065.8  36319.2  13171.6  7006.58   

country        Costa Rica     Cuba Dominican Republic  Ecuador    ...     \
gdpPercap_1997    6677.05  5431.99             3614.1  7429.46    ...      
gdpPercap_2002    7723.45  6340.65            4563.81  5773.04    ...      
gdpPercap_2007    9645.06   8948.1            6025.37  6873.26    ...      

country          Mexico Nicaragua   Panama Paraguay     Peru Puerto Rico  \
gdpPercap_1997   9767.3   2253.02  7113.69   4247.4  5838.35     16999.4   
gdpPercap_2002  10742.4   2474.55  7356.03  3783.67  5909.02     18855.6   
gdpPercap_2007  11977.6   2749.32  9809.19  4172.84  7408.91     19328.7   

country        Trinidad and Tobago United States  Uruguay Venezuela  
gdpPercap_1997             8792.57       35767.4  9230.24   10165.5  
gdpPercap_2002             11460.6       39097.1     7727   8605.05  
gdpPercap_2007             18008.5       42951.7  10611.5   11415.8  

Note: we could have done the above in a single line of code by 'chaining' the commands:

americas.T.tail(n=3)

