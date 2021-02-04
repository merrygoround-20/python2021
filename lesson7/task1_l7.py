#  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f'{i:4}', end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(other.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [1, 2, 3], [1, -1, -1], [-1, -1, -1]])
new_m = Matrix([[-2, 0, 2], [1, 1, 2], [0, 0, 0], [-3, -2, 3]])
print(f'{m + new_m}')

m = Matrix([[1, 2, 3], [1, 2, 3], [1, -1, -1]])
new_m = Matrix([[-2, 0, 2], [1, 1, 2], [0, 0, 0]])
print(f'\n{m + new_m}')
