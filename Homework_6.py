import numpy as np


class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        rows = [" ".join([str(self._matrix[i][j]) for j in range(self._columns)]) for i in range(self._rows)]
        with open(filename, 'w') as f:
            f.write("\n".join(rows))

    def traspose(self):
        """
        Transpose the matrix.
        TODO: implement
        """
        return [[row[i] for row in self._matrix] for i in range(self._columns)]

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        if self._columns != other._columns or self._rows != other._rows:
            raise ValueError("Matrices can only be added if the dimensions are the same")

        return [[self._matrix[i][j] + other._matrix[i][j] for j in range(self._columns)] for i in range(self._rows)]

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        if not isinstance(other, Matrix):
            return [[self._matrix[i][j] * other for j in range(self._columns)] for i in range(self._rows)]

        elif self._columns != other._columns or self._rows != other._rows:
            raise ValueError("Matrices can only be added if the dimensions are the same")

        return [[self._matrix[i][j] * other._matrix[i][j] for j in range(self._columns)] for i in range(self._rows)]

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """
        if self._columns != other._rows:
            raise ValueError("The width of the first matrix is the same as the height of the second matrix")

        return [[sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other._matrix)]
                for self_row in self._matrix]

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        if self._rows != self._columns:
            raise ValueError("Cannot calculate the trace of a non-square matrix.")

        return sum(self._matrix[i][i] for i in range(self._rows))

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        if self._rows != self._columns:
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")

        return np.linalg.det(self._matrix)
