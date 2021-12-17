#leetcode Top K Frequent solution 
from collections import Counter

def topKFrequent(nums,k):
    l=[]
    d = Counter(nums)
    print(d)
    h = d.most_common(k)
    print(h)
    print(d)
    for i in range(len(h)):
        l.append(h[i][0])
    return l

print(topKFrequent([1,1,1,2,2,3,3,3,3],3))