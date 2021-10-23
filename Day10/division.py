
def div(num1 , num2):
   
    trysubstr = ''
    #first if the number is greater than the divider
    if num1 < num2:
        # no need to check the length just add 0 at the end
        num1s = str(num1) + '0'
        num1 = int(num1s)
        result = '0.'
        
    else: 
        num1 = num1
        result = ''
  
    while num1 >= num2:#12 / 10
        if len(str(num1)) >= len( str(num2)) :
            trydiv = num1//num2
            trymulti = trydiv * num2
           
            trysub = num1 - trymulti
            result += str(trydiv)
            if trysub < num2 and trysub != 0:
                trysubstr = str(trysub) + '0'
                
                num1 = int(trysubstr)
                if '.' not in result:
                    result += '.'
            else:
                num1 = trysub
  
    return result
print(div(122 , 122))