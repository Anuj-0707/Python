def print_list(list, idx=0):
    if (idx==len(list)):
        return 
    print(list[idx],end=" ")
    print_list(list,idx+1)
heroes = ["Rajesh","Anul","ompuri","akshay","Ajay"]
print_list(heroes)