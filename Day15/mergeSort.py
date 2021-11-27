
# Merge Sort algorithm 

class Merge:
    def __init__(self, numS, lb,ub):
        self.numS= numS
        self.lb= lb
        self.ub= ub
def merge_sort(numS):
    if len(numS) > 1:
        mid = (len(numS))//2
        list1 = numS[:mid]
        list2=numS[mid:]
        print(list1)
        print(list2)
        merge_sort(list1)
        merge_sort(list2)

        # if lb < ub:
        #     merge_sort(numS, lb,mid)
        #     merge_sort(numS, mid+1,ub)
            
    
        i = 0    
        j = 0
        k = 0
        while i < (len(list1)) and j <len(list2):
            if list1[i] < list2[j]:
                numS[k]= list1[i]
                i+=1
                
            else:
                numS[k]= list2[j]
                j+=1
            k+=1
        while i < len(list1):
            numS[k]= list1[i]
            i+=1
            k+=1

        while j < len(list2):
            numS[k] = list2[j]
            j+=1
            k+=1
        
        
        print(numS)
    # numS[:] = list2
    return numS


# list1 = Merge([5,2,4,1],0,3)
print(merge_sort([5,2,4,1]))




    

