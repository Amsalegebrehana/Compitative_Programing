#factors of an intiger
import time
time1 = time.time()
print(time1)
l=[]
num = 48
div = 2
while div < 10:
    if num % div == 0:
        print(div, end =",")
        num=num/div
    else:
        div +=1
        # num=num/div
print()
time2 = time.time()
print(time2)