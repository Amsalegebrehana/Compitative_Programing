class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0,-1)
        heights.append(-1)
       
        max_area = 0
        st = []
        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                x = st.pop()
                max_area= max(max_area, (i - st[-1] -1) * heights[x])
            st.append(i)
        return max_area