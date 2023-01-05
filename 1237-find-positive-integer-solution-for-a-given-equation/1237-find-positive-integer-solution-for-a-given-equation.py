"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
            x = 1
            y = z
            result = []
            while y > 0 and x < z+1:
                if customfunction.f(x,y) > z:
                    y -= 1
                elif customfunction.f(x,y) < z:
                    x +=1
                else:
                    result.append([x,y])
                    x+=1
                    y-=1

            return result
