# Function works on the old wheat/rice story, 1 grain on the first day, 2 on the second, 4 on the third,
# and so on, doubling the value of the last number to get the next one. This function takes a grain number
# and returns how many iterations of this sequence must occur to get to desired number of grains.
# Testing is done through /Test_basic.
def squares_needed(grains):
    i = 1
    j = 0
    counter = 0
    while(counter < grains):
        counter += i
        i *= 2
        j += 1
    return(j)