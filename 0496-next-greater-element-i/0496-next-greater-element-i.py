class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        st = []
        result = [-1] * n
        for i in range(n-1, -1, -1):
            while st and st[-1] < nums2[i]:
                st.pop()
            if st:
                result[i] = st[-1]
            st.append(nums2[i])

        dictt = {}
        for i in range(n):
            dictt[nums2[i]] = result[i]
    
        ans = []
        for i in nums1:
            ans.append(dictt[i])
        return ans