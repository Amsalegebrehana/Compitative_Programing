def two_sum(my_num, target):
    output = []
    len1 = len(my_num)
    first = 0
    second = 0
    num_check = 1
    for i in range (len1):
        if num_check < len1:
            first = my_num[i]
            second = my_num[num_check]
            num_check += 1
            result = first + second
            if result == target:
                if first == second:
                    n1 = my_num.index(first)
                    n2 = n1 + 1
                    output.append(n1)
                    output.append(n2)
                else:     
                    n1 = my_num.index(first) 
                    n2 = my_num.index(second) 
                    output.append(n1)
                    output.append(n2)
    return output

print(two_sum([1,2,4],6))

