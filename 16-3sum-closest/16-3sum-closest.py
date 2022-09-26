class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        result = float("inf")
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) -1 
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(target - temp) < ans :
                    ans = abs(target - temp)
                    result = temp
                if temp < target:
                    j += 1
                elif temp > target:
                    k-=1
                else:
                   
                    return temp
                
       
        return result