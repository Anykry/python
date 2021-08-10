class Cell:
    def __init__(self, nucleus):
        self.__nucleus = nucleus

    def __add__(self, other):
        return self.__nucleus + other.__nucleus

    def __sub__(self, other):
        if self.__nucleus - other.__nucleus > 0:
            return self.__nucleus - other.__nucleus
        else:
            return f'Can not perform subtraction'

    def __mul__(self, other):
        return Cell(self.__nucleus * other.__nucleus)

    def __truediv__(self, other):
        return Cell(round(self.__nucleus / other.__nucleus, 0))

    def make_order(self, count):
        iter = self.__nucleus // count

        i = 1
        st = '*'
        while i <= iter:
            st *= count
            st = st + '!'
            i += 1
        st = st + (count - iter*count)*'*'
        print(st)


my_cell = Cell(12)
print(my_cell.make_order(5))