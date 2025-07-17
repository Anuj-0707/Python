# Continue terminates execution in the current iteration and continues execution of the loop with the next iteration
i=0
while i<=5:
    if(i==3):
        i+=1
        continue # skip
    print(i)
    i+=1