coll = {1,2,3,4,5}
coll.add(6)
print(coll)
coll.add((1,2,3))
coll.add("Anuj")
print(coll)
#coll.add([1,2,3,4]) # we cannot add list and dictionary in set
# unhashable
print(len(coll))
print(coll.pop())
set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))