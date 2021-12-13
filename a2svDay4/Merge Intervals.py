

def mergeIntervals(intervals ):
    intervals = sorted(intervals)  
    i=0
    while(i<len(intervals)-1):


        if  intervals[i][1] >= intervals[i+1][0]:
            
            if intervals[i+1][1] > intervals[i][1]:
                
                k = intervals[i+1][1]
            else:
                k= intervals[i][1]
            x = [intervals[i][0],k ]
            intervals.remove(intervals[i+1])
            intervals.remove(intervals[i])
            intervals.insert(i,x)
        else:

            i+=1
        # print(l)


     
    return intervals
print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
                
    