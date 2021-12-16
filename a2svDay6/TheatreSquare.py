#codeforces solution

import math
def theatreSquare(m, n, a):
    x= math.ceil(n/ a)
    # print(x)
    y = math.ceil(m/ a)
    # print(y)
    return x*y
    


# test_case = input()
# nums = test_case.split(' ')
m, n, a= map(int, input().split())
print(theatreSquare(m, n, a))