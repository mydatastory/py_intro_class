def string_machine(input_string, iterations):
    """
    Takes input_string and generates a new string with -'s and *'s
    corresponding to characters that have identical adjacent characters
    or not, respectively.  Iterates through this procedure with the resultant
    strings for the supplied number of iterations.
    """
    print(input_string)
    old = input_string
    for i in range(iterations):
        new = ''
        # iterate through characters in previous string
        for j in range(len(input_string)):
            left = j-1
            right = (j+1)%len(input_string) # ensure right index wraps around
            if old[left]==old[right]:
                new += '-'
            else:
                new += '*'
        print(new)
        # store new string as old
        old = new

string_machine('et cetera', 10)