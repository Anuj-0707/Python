f = open("chapter7\intro.txt","r")
for i in range(7):
    linei=f.readline()
    print(linei,end="")
f.close()