names = ["Nil", "Jil", "Kil", "Lil", "Paramita"]
il_name = [name for name in names if "il" in name]
print(il_name)

tea = {
    "masala chai",
    "green tea",
    "black tea",
    "oolong tea",
    "white tea",
    "herbal tea",
    "matcha",
}
chai_name = {chai for chai in tea if "chai" in chai}
print(chai_name)

recipes = {
    "Masala chai": ["ginger", "cardemom", "cloves"],
    "Ginger chai": ["cardemom", "milk"],
    "Spicy Chai": ["ginger", "cardemom", "cloves", "pepper"],
}
unique = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique)

tea_prices = {
    "masala": 80,
    "green": 50,
    "black": 60,
    "oolong": 70,
    "white": 40,
    "herbal": 30,
    "matcha": 90,
}

tea_with_price = {tea: price / 80 for tea, price in tea_prices.items()}
print(tea_with_price)


#  Generator comprehensions
numbers = [1,2,3,4,5,6,7]
print(sum(num for num in numbers if num > 5))