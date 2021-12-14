import numpy as np
import src.maths.matrix_decompositions as md


class QRDiagonalisation:
    def __init__(self, A, nitermax):
        self.A = A
        self.Qk = None
        self.Rk = None
        self.Akpp = None
        self.iter = 0
        self.nitermax = nitermax
        self.temp_list = []
        self.QR = md.QR(self.A)

    def diagonalisation_method(self):
        k = 0
        n, p = np.shape(self.A)
        Q = self.QR.decomposition()[0]
        R = self.QR.decomposition()[1]

        while self.iter < self.nitermax:
            self.iter += 1
            if k == 0:
                Ak = self.A
            else:
                Ak = self.Akpp

            self.Qk = np.linalg.matrix_power(Q, k)
            self.Rk = np.linalg.matrix_power(R, k)
            self.Akpp = np.dot(self.Rk, self.Qk)

            for i in range(0, n - 1):
                for j in range(i + 1, n - 1):
                    self.temp_list.append(np.abs(self.Akpp[j, i]))

            print("k =", k)
            print("Qk =", self.Qk)
            print("Rk =", self.Rk)
            print("Akpp =", self.Akpp)
            print("temp list =", self.temp_list, "\n")

            k += 1


###

A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
test = QRDiagonalisation(A, nitermax=100)
print(test.diagonalisation_method())

