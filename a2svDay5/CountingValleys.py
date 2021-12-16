#hackerrank Counting Valleys solution 


def countingValleys(steps, path):
    count=0
    valley = 0
    for i in range(0, steps):
        if path[i] == 'U':
            count+=1
            if count==0:
                valley+=1
        elif path[i] == 'D':
            count-=1
    return valley

print(countingValleys(8,"UDDDUDUU"))



