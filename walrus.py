val = 13


# remainder = val % 2

# if remainder:
#     print("Not divisible")

if rem := val % 2:
    print("Not divisible")


available = ["large", "medium", "small"]
if requested_size := input("Enter your size: "):
    print(f"serving {requested_size} from available sizes")
