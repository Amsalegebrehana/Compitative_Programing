# leetcode 278 First bad Version solution

  def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        badStart = False
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid) == True and isBadVersion(mid- 1) == True:
                right = mid - 1
            if isBadVersion(mid) == True and isBadVersion(mid- 1) == False:
                return mid
            elif isBadVersion(mid) == False:
                left = mid +1
        