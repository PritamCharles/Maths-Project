import numpy as np


class Matrix:
    def __init__(self, size):
        self.size = size

    def SDPmatrix(self, mat):
        if np.linalg.det(mat) != 0:
            A = np.dot(np.transpose(mat), mat)
            return A
        else:
            print("La matrice n'est pas inversible.")

    def hilbert_matrix(self):
        mat = np.zeros((self.size, self.size))
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                mat[j - 1, i - 1] = 1 / (i + j - 1)
        return mat

    def int_random_matrix(self):
        mat = np.random.randint(1, 11, (self.size, self.size))
        return self.SDPmatrix(mat)

    def random_matrix(self):
        mat = np.random.randn(self.size, self.size) ** 2
        return self.SDPmatrix(mat)
