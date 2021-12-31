import numpy as np
from sympy import *
import src.maths.utils.matrix_decompositions as md


class QRDiagonalisation:
    def __init__(self, A, nitermax, epsilon):
        self.A = A
        self.Qk = None
        self.Rk = None
        self.Akpp = None
        self.iter = 0
        self.epsilon = epsilon
        self.nitermax = nitermax
        self.QR = md.QR(self.A)

    def diagonalisation_method(self):
        k = 0
        n, p = np.shape(self.A)
        eigval_list = []

        while self.iter < self.nitermax:
            self.iter += 1

            Q = self.QR.decomposition()[0]
            R = self.QR.decomposition()[1]

            if k == 0:
                Ak = self.A
            else:
                Ak = self.Akpp

            self.Akpp = np.dot(R, Q)

            """for j in range(0, n):
                for i in range(0, n):
                    if i > j:
                        if Ak[i, j] > self.epsilon:
                            break"""
            k += 1

        for i in range(n):
            eigval_list.append(self.Akpp[i, i])

        return k, self.Akpp, eigval_list


###

A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
test = QRDiagonalisation(A, nitermax=100, epsilon=10 ** 20)
print(test.diagonalisation_method())
