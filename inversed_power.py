import utils.create_matrix as cm
import utils.matrix_decompositions as md
import numpy as np


class InversedPower:
    def __init__(self, A, nitermax, epsilon):
        self.A = A
        self.A_gap = None
        self.x = np.random.random(len(A))
        self.wkpp = None
        self.gap_wkpp = None
        self.eigval = None
        self.gap_eigval = None
        self.nitermax = nitermax
        self.iter = 0
        self.epsilon = epsilon
        self.answer = int(input(
            "Nous utilisons les décompositions pour calculer la plus petite valeur propre.\n1 - Décomposition de Cholesky\n2 - Décomposition LU\n3 - Décomposition QR\nLaquelle chosissez vous (numéro en réponse)?"))

    def inversed_power_method(self):
        cholesky = md.Cholesky(A)
        lu = md.LU(A)
        qr = md.QR(A)
        k = 0

        while self.iter <= self.nitermax:
            self.iter += 1
            if k == 0:
                wk = self.x / np.linalg.norm(self.x)
            else:
                wk = self.wkpp

            if self.answer == 1:
                mat_1 = cholesky.decomposition()[0]
                mat_2 = cholesky.decomposition()[1]
            elif self.answer == 2:
                mat_1 = lu.decomposition()[0]
                mat_2 = lu.decomposition()[1]
            elif self.answer == 3:
                mat_1 = qr.decomposition()[0]
                mat_2 = qr.decomposition()[1]

            y_int = np.linalg.solve(mat_1, wk)
            ck = np.linalg.solve(mat_2, y_int)
            self.wkpp = ck / np.linalg.norm(ck)

            if self.wkpp is not None:
                self.diff = np.linalg.norm(self.wkpp - wk)

                if self.diff <= self.epsilon:
                    break

            self.eigval = 1 / np.linalg.norm(ck)
            k += 1

        return k, self.wkpp, self.eigval, self.diff

    def gap_method(self, gamma):
        self.A_gap = self.A - np.dot(gamma, np.eye(len(self.A)))

        if np.linalg.det(self.A_gap) != 0:
            A = np.dot(np.transpose(self.A_gap), self.A_gap)
            return A
        else:
            print("La matrice n'est pas inversible.")

        cholesky = md.Cholesky(self.A_gap)
        lu = md.LU(self.A_gap)
        qr = md.QR(self.A_gap)
        k = 0

        while self.iter <= self.nitermax:
            self.iter += 1
            if k == 0:
                wk = self.x / np.linalg.norm(self.x)
            else:
                wk = self.wkpp

            if self.answer == 1:
                mat_1 = cholesky.decomposition()[0]
                mat_2 = cholesky.decomposition()[1]
            elif self.answer == 2:
                mat_1 = lu.decomposition()[0]
                mat_2 = lu.decomposition()[1]
            elif self.answer == 3:
                mat_1 = qr.decomposition()[0]
                mat_2 = qr.decomposition()[1]

            y_int = np.linalg.solve(mat_1, wk)
            ck = np.linalg.solve(mat_2, y_int)
            self.wkpp = ck / np.linalg.norm(ck)

            if self.wkpp is not None:
                self.diff = np.linalg.norm(self.wkpp - wk)

                if self.diff <= self.epsilon:
                    break

            self.eigval = 1 / np.linalg.norm(ck)
            k += 1

        return k, self.wkpp, self.eigval, self.diff


###

matrix = cm.Matrix(size=6)
# A = matrix.random_matrix()
A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
test = InversedPower(A, nitermax=100, epsilon=10 ** (-16))
"""print("k =", test.inversed_power_method()[0])
print("approximation vecteur propre =", test.inversed_power_method()[1])
print("plus petite valeur =", test.inversed_power_method()[2])
print("difference =", test.inversed_power_method()[3])
print(np.linalg.eig(A))"""

print("k =", test.gap_method(gamma=2)[0])
print("approximation vecteur propre =", test.gap_method(gamma=2)[1])
print("plus petite valeur propre =", test.gap_method(gamma=2)[2])
print("difference =", test.gap_method(gamma=2)[3])
print(np.linalg.eig(A))

###