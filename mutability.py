obj1 = {
    "name": "Niladri",
    "age": 25
}
obj2 = obj1
obj2["age"] = 26
print(obj1["age"])  # Output: 26
obj3 = obj1.copy()
obj3["age"] = 27
print(obj1["age"])  # Output: 26