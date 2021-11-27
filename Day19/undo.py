# undo implementation in python I will implement it by java too

def undo():
    ele_list = []
    enter = ''
   
    while enter != 'exit':
        enter = input("Enter: ")
        ele_list.append(enter)
       
        if enter == "undo":
            ele_list.pop()
            ele_list.pop()
            print(ele_list)
        
    if enter == 'exit':
        ele_list.pop()    
        print(ele_list)
      
        exit()
    return ele_list

print(undo())
        
        