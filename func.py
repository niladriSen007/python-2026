def outer():
    val = "Nil"

    def inner():
        val = "Nilaaa"
        print(f"{val}")

    print(f"{val}")
    inner()


outer()
