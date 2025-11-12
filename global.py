name = "Nil"


def outer():
    global name
    name = "Paro"
    print(f"Inside outer:{name}")

    def inner():
        global name
        name = "Paramita"
        print(f"Inside inner:{name}")

    print(f"Outside inner:{name}")
    inner()
    print(f"Outside outer:{name}")

outer()
print(name)