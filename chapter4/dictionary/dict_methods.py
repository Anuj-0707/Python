student={
    "name":"Anuj Pandey",
    "subjects": {
        "phy":97,
        "maths":95,
        "chem":90,
        "geo":98,
        "hist":99
    }
}
print(student.keys()) # it printall the keys except the nested keys
print(len(student)) # it gives totalnumber of keys avoid the nested one
print(list(student.keys())) # it give output of list of keys
print(student.values()) # it gives all values
print(student.items()) # returns all (key,value) pairs as tuples
print(student.get("name"))# return the value according to the key
student.update({"city":"Gorakhpur"}) # inserts the specified items to the dictionary
student.update({"name":"Satyam Pandey"})
print(student)