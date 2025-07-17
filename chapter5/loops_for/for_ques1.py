num=(1,2,3,4,5,6,7,8,9,9,4,9)
x=int(input("Enter number to find : "))
i=0
for el in num:
    if el==x:
        print("number found at index",i)
    i+=1