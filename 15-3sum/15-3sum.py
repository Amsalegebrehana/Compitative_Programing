class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans =[]
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) -1
            while j <= k:
                
                if nums[i] + nums[j] + nums[k] >0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if i != j and i != k and j != k:
                        temp = [nums[i], nums[j], nums[k]]
                      
                        if temp not in ans:
                            ans.append(temp)
                    j += 1
                    k-=1
        return ans