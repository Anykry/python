class Cell:
    def __init__(self, nucleus):
        self.__nucleus = nucleus
        self.count = nucleus

    def __str__(self):
        return f'{self.__nucleus}'

    def __add__(self, other):
        return Cell(self.__nucleus + other.__nucleus)

    def __sub__(self, other):
        if self.__nucleus - other.__nucleus >= 0:
            return Cell(self.__nucleus - other.__nucleus)
        else:
            return f'Can not perform subtraction'

    def __mul__(self, other):
        return Cell(self.__nucleus * other.__nucleus)

    def __truediv__(self, other):
        return Cell(round(self.__nucleus / other.__nucleus, 0))

    def make_order(self, count):
        iter = self.__nucleus // count
        i = 1
        final_str = ''
        while i <= iter:
            st = '*'
            st *= count
            st = st + '\n'
            i += 1
            final_str += st
        final_str = final_str + (self.__nucleus - iter*count)*'*'

        return final_str


my_cell = Cell(12)
print(my_cell.make_order(5))

my_cell2 = Cell(5)
my_cell3 = my_cell + my_cell2
print(my_cell3)