# hackerrank String Split and Join solution

def splitJoin(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
    
print(splitJoin("this is a string"))