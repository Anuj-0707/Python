n = int(input("Enter a number"))
i=1
fact=1
facto=1
while i<=n:
    fact*=i
    i+=1
print(fact)
                         #OR
for x in range(1,n+1):
    facto*=x
    x+=1
print(facto)