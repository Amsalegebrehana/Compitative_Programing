class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []
        result = [-1] * n 
        for i in range(2 * n - 1, -1 , -1):
            while st and st[-1] <= nums[i%n]:
                st.pop()
            if st:
                result[i%n] = st[-1]
            st.append(nums[i % n])
        return result