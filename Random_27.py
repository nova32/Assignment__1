#investment calculator

#event list:

#take money from people and return it in a specific amount of time - check
#ex: input '10k' ask: how many years for investment. - check

#if they input less than 5k 3% back, less than 5k 5% back, over 10k 8% back per year
#output the amount of money they'd have after specific time


import cmath
#import math library


userin = float(input('Enter the amount of money you want to invest in us.\n(5k or less = 3%, 8k or less = 5% back, over 10k = 8% back per year\n'))
#Gather user input (money)

timeinv = int(input('Enter the number of years you want to invest in us.\n'))
#Gather user input (time)


if userin <= 5000:
    #statement comparing user value less than target

    fstplan = userin * (1 + 0.03/1)**(1*timeinv)
    print("Balance after ", timeinv, " year/s" " $", "%.2f" % fstplan)
    #output of value equal to or less than $5000. First plan
    

elif userin >= 5000 and userin <= 10000:
    #statement comparing user value. Greater than 5000 less than 10000

    scndplan = userin * (1 + 0.05/1)**(1*timeinv)
    print("Balance after ", timeinv, " year/s" " $", "%.2f" % scndplan)
    #output of value greater than or equal $5000 and less than or equal to $10000. Second plan


elif userin >= 10000:
    #statement comparing user value greater than target

    thdplan = userin * (1 + 0.08/1)**(1*timeinv)
    print("Balance after ", timeinv, " year/s" " $", "%.2f" % thdplan)
    #output of value equal to or greater than $10000. Third plan





