class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prexSum = [cardPoints[0]]
        runSum = 0
        maxSum = 0
        for i in range(1,k):
            prexSum.append(prexSum[-1] + cardPoints[i])
        maxSum = prexSum[k-1]
        count = 1

        for i in range(len(cardPoints) - 1, -1, -1):
            if count ==  k:
                runSum += cardPoints[i]
                break
            runSum += cardPoints[i]
            maxSum = max(maxSum, prexSum[k - count - 1] + runSum)
            count +=1
        maxSum = max(maxSum, runSum )

        return maxSum
