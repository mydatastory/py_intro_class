def print_egg_label(mass):
    #egg sizing machinery prints a label
    if(mass>=90):
        return("warning: egg might be dirty")
    elif(mass>=85):
        return("jumbo")
    elif(mass>=70):
        return("large")
    elif(mass<70 and mass>=55):
        return("medium")
    elif(mass<50):
        return("too light, probably spoiled")
    else:
        return("small")