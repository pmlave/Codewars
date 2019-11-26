def squares_needed(grains):
    i = 1
    j = 0
    counter = 0
    while(counter < grains):
        counter += i
        i *= 2
        j += 1
    return(j)