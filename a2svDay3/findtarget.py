 def targetIndices(numstarget) :
        l=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        for i in range(0,len(nums)):
            if nums[i] == target:
                l.append(i)
        print(nums)
        return l
print(targetIndices())