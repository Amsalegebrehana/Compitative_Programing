#hackerRank Find the median solution

class Median:
    def __init__(self, arr):
        self.arr = arr
    def sort(self):
        for i in range(len(self.arr)):
            for j in range(i,len(self.arr)):
                if self.arr[i] > self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr
    def median(self):
        self.sort()

        return self.arr[len(self.arr)//2]

arrsort = Median([5,6,1,2,4])
print(arrsort.sort())
print(arrsort.median())
