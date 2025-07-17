n = int(input("Enter a number : "))
i=1
sum=0
sum1=0
while i<=n:
    sum+=i
    i+=1
print(sum)

                        # OR
for x in range(1,n+1):
    sum1+=x
    x+=1
print(sum1)