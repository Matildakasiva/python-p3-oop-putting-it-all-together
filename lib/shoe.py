#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        pass
        self.brand = brand
        self.size = size
        self.condition = "New"
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("not an integer")
            raise TypeError("size must be an integer")
        self._size = value