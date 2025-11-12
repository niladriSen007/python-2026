def outer():
    val = "Nil"

    def inner():
        nonlocal val
        val = "Nilaaa"
        print(f"Inside :{val}")

    inner()
    print(f"Outside :{val}")


outer()
