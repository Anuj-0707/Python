# tuples are immutable
# uses parenthesis
tup=(2, 3, 4, 5)
print(tup[3])
print(type(tup))
tup1=(4)
print(type(tup1))
# for tup1 output will be int type because python thinks it is an integer value surrounded by parenthesis
#to resolve it we will use , in single element tuple
tup2=(4,) 
print(type(tup2))