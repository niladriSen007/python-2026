class Parent:
    def __init__(self, name, age, height):
        self.name = name
        self._height = height
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age must be positive")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.__age}, Height: {self._height}"

    def __repr__(self):
        return f"Parent(name='{self.name}', age={self.__age}, height={self._height})"
        
father = Parent("John", 40, 180)
print(father)
print(father.get_age())