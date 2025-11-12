users = [
    {"id": 1, "total": 100, "coupon": "p10"},
    {"id": 2, "total": 400, "coupon": "f10"},
    {"id": 3, "total": 100, "coupon": "c10"},
]

discount = {"p10": (0.2, 0), "f10": (0.5, 0), "c10": (0, 10)}

for user in users:
    percent, fixed = discount.get(user["coupon"], (0, 0))
    print(f"User {user['id']} has {percent*100} percent discount with fixed price Rs.{fixed}")
