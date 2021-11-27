#hackerRank mutation solution

def mutate_string(string, position, character):
    str1 = string[:position]
    str2 = string[position:]
    str2 = str2.replace(str2[0],character,1)
    
    result = str1 + str2
    
    return result
    
print(mutate_string("abracadabra", 5, 'k'))