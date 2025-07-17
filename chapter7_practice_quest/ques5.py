with open("Numero.txt","r") as f:
    count=0
    data=f.read()
    print(data)
    num=data.split(",")
    print(num)
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count)
     
''' num = ""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num = ""
        else:
            num += data[i]'''
