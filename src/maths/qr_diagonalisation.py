import numpy as np
import src.maths.utils.matrix_decompositions as md


class QRDiagonalisation:
    def __init__(self, A, nitermax, epsilon):
        self.A = A
        self.P = None
        self.Ak = None
        self.Akpp = None
        self.Mk = None
        self.Q = None
        self.R = None
        self.iter = 0
        self.epsilon = epsilon
        self.nitermax = nitermax
        self.state = True

    def diagonalisation_method(self):
        k = 0
        n, p = np.shape(self.A)
        eigval_list = []

        while (self.iter < self.nitermax) and self.state:
            self.iter += 1
            if k == 0:
                self.Ak = self.A
            else:
                self.Ak = self.Akpp

            self.QR = md.QR(self.Ak)
            self.Q = self.QR.decomposition()[0]
            self.R = self.QR.decomposition()[1]
            self.Akpp = np.dot(self.R, self.Q)
            self.P = np.dot(np.dot(np.transpose(self.Q), self.Ak), self.Q)

            mk_list = []
            for i in range(n):
                for j in range(n):
                    if j < i:
                        mk_list.append(np.abs(self.Ak[i, j]))
                        if np.abs(self.Ak[i, j]) <= self.epsilon:
                            self.state = False

            self.Mk = max(mk_list)

            k += 1

        for i in range(n):
            eigval_list.append(self.Ak[i, i])

        return k, self.Ak, eigval_list, self.Mk, self.P

    def numpy_eig(self, mat):
        return np.linalg.eig(mat)


###

"""A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
qrdiag = QRDiagonalisation(A, nitermax=100, epsilon=10 ** (-16))
print("A =", A)
print("Nombre d'itérations =", qrdiag.diagonalisation_method()[0])
print("Dernière matrice A calculée =", qrdiag.diagonalisation_method()[1])
print("Approximation des valeurs propres =", qrdiag.diagonalisation_method()[2])
print("Plus grand coefficient en-dessous de la diagonale =", qrdiag.diagonalisation_method()[3])
print("Matrice de passage P =", qrdiag.diagonalisation_method()[4])
# print("numpy:", qrdiag.numpy_eig(A))
"""
###