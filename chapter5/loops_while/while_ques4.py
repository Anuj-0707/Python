tup=(1,4,9,16,25,36,49,64,81,100)
i=0
x=int(input("Enter a number to search : "))
while i<=len(tup)-1:
    if tup[i]==x:
        print(x,"Exist in the tuple at index",i)
    i+=1