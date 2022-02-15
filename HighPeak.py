import random
while(1):
    tgoodies={'fitbitplus':7980, 'ipod':22349, 'miband':999, 'cultpass':2799, 'macbookpro':229900,
              'digitalcamara':11101, 'alex':9999,'sandwichroaster':2195,'microwave ovan':9800,
              'scale':4999}   #storiing goodies using dictionary
    b=list()
    c=list()                   #creating list
    goodieslist=list(tgoodies)   #converting dictionary to list because in dict we cannot use random function                  

    employee=int(input("enter number of employee "))      #taking input from the user
    for i in range(1, employee+1):
        b.append(random.choice(goodieslist))        #choosing gift using random function and appending it into list b          
    for i in range (0, employee):
        print(b[i],":",tgoodies.get(b[i]))         #printing appended key and values of that key present in dictonary using get function
        c.append(tgoodies.get(b[i]))            #appending the value of keys to the list c
    
    maximum=max(c)                          #finding maximum value from choosen goodies
    minimum=min(c)                          #finding minimum value from choosen goodies
    difference=maximum-minimum              #finding the difference between maximum and minimum
    print("and the difference between the chosen goodies with highest price and the lowest price is",difference)
