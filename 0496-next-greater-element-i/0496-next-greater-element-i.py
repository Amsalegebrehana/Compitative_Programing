class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapp = {}
        
        for num in nums2:
            
            while(stack and num > stack[-1]):
                c = stack.pop()
                mapp[c] = num
            
            stack.append(num)
  
        return [mapp.get(num, -1)  for num in nums1 ]