age = int(input("Enter you age : "))
if(age>=18):
    print("You can vote")
    if(age>=80):
        print("But you can not drive")
    else:
        print("You can drive also")
else:
    print("You can neither vote nor drive")