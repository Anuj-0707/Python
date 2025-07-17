list = [1,4,7,5,8,9,6,3]
list.append(10) #adds oneelement atthe end
print(list)
list.sort() #sorts in ascending order
print(list)
list.sort(reverse=True) #sorts in descending order
print(list)
list.reverse() #reverse list
print(list)
#list.insert(idx,el) insert element at index
list.insert(4,73)
print(list)
#list.remove(el) removes the first occurence of elememnt
list.remove(5)
print(list)
#list.pop(idx) removes element at given index
list.pop(3)
print(list)
