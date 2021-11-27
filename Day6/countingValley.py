#hacker rank Counting Valley solution

def countValley(steps, path):
    l=[]
    origin = 0
    valley = 0
    isValley = False
    for i in path:
        if i == 'U':
            l.append(1) # add all U's as 1 in a list
        elif i== 'D':
            l.append(-1)# add all D's as -1 in a list
    for i in range(steps):
        origin += l[i] # add all numbers
        print(origin)
        if origin < 0 and not isValley: # if origin is below zero then it is inside the valley
            isValley = True # still inside valley
        elif origin == 0 and isValley:
            
            valley +=1 # if origin is zero the count the valley 
            isValley = False # set valley to false cause  it is out of the valley as origin is 0


    print( l)
    return valley

print(countValley(12,'DDUUDDUDUUUD'))
