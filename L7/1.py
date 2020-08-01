class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        if len({len(row) for row in self.matrix}) == 1:
            return '\n'.join(map(str, ['\t'.join(map(str, [el for el in row])) for row in self.matrix]))
        else:
            return 'Матрица задана некорректно!'
        # matrix_string = ''
        # for row in self.matrix:
        #     for el in row:
        #         matrix_string += f"{el}\t"
        #     matrix_string += '\n'
        # return matrix_string

    def __add__(self, other):
        if {len(row) for row in self.matrix} == {len(row) for row in other.matrix}:
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in
                           range(len(self.matrix))])
            # new_matrix = []
            # for i in range(len(self.matrix)):
            #     new_matrix.append([])
            #     for j in range(len(self.matrix[i])):
            #         new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
            # return Matrix(new_matrix)
        else:
            return 'Операция суммы не определена, так как различаются размерности матриц!'


my_matrix1 = Matrix([[1, 4, 7], [2, 1, 4], [3, 1, 2]])
my_matrix2 = Matrix([[6, 3, 0], [5, 1, 5], [2, 6, 1]])
my_matrix3 = my_matrix1 + my_matrix2
print(f"Матрица 1:\n{my_matrix1}\n")
print(f"Матрица 2:\n{my_matrix2}\n")
print(f"Матрица 3:\n{my_matrix3}\n")
