def makeChai(chai: str, milk: str, sugar: bool):
    print(f"Making {chai} with, {milk}, and {'with' if sugar else 'without'} sugar...")


makeChai(chai="chai", milk="milk", sugar=False)

print("---------Args and Kwargs-------------")


def special_chai(*ingredients, **extras):
    print(f"Ingredients - {ingredients}")
    print(f"Extras - {extras}")


special_chai("Milk", "Sugar", "Cream", "Chocolate", sugar="low", cream="medium")

print("---------Multiple Return Values-------------")


def multiple_return_values():
    return 1, 2, 3


a, b, c = multiple_return_values()
print(a, b, c)

