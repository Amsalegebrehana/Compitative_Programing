# 2170. Minimum Operations to Make the Array Alternating
from typing import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        odd = Counter(nums[1::2]).most_common()
        sizeodd = len(nums) // 2
        even = Counter(nums[::2]).most_common()
        sizeeven = len(nums)//2 if len(nums)%2 ==0 else (len(nums)//2) +1
       
        if even[0][0] != odd[0][0]:
            return (sizeeven - even[0][1]) + (sizeodd - odd[0][1])
        else:
            
            if len(odd)==len(even)==1:
                return min(odd[0][1],even[0][1])
            elif len(odd) > 1 and len(even) > 1:
                minn = min((sizeeven - even[0][1] + sizeodd - odd[1][1]),(sizeeven - even[1][1] + sizeodd - odd[0][1]))
                return minn
            elif len(odd) == 1 and len(even) > 1:
                return (sizeodd - odd[0][1]) + (sizeeven - even[1][1])
            elif len(odd) > 1 and len(even) == 1:
                return (sizeodd - odd[1][1]) + (sizeeven - even[0][1])
        