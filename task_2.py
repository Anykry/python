from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def clothes_quantity(self):
        pass

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def clothes_quantity(self):
        return 2 * self.height + 0.3


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def clothes_quantity(self):
        return self.size / 6.5 + 0.5


my_coat = Coat(48)
my_suit = Suit(40)

print(my_suit.clothes_quantity + my_coat.clothes_quantity)

