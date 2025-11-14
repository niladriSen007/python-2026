add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
print("---------Lambda Functions-------------")
print("Addition:", add(5, 3))
print("Subtraction:", sub(5, 3))
print("Multiplication:", mul(5, 3))
print("Division:", div(5, 3))

chai = ["strong", "kadak", "kadak", "kadak"]
strong_chai = list(filter(lambda chai: chai == "strong", chai))
print(strong_chai)
print(chai)
