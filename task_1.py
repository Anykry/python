class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        row = ''
        for el in self.matrix_list:
            row += f'{el}'+'\n'
        return row

    def __add__(self, other):
        new_matrix = []
        for i, el in enumerate(self.matrix_list):
            new_line = []
            for k, row in enumerate(el):
                new_line.append(row + other.matrix_list[i][k])
            new_matrix.append(new_line)
        return new_matrix


my_matrix = Matrix([[31, 22, 12], [37, 43, 5], [51, 86, -6]])
my_matrix2 = Matrix([[2, 4, 1], [3, 3, -2], [19, 7, 13]])
print(my_matrix)

sum_matrix = Matrix(my_matrix + my_matrix2)
print(sum_matrix)
