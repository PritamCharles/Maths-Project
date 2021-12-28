import numpy as np
import src.maths.matrix_decompositions as md


class InversedPower:
    def __init__(self, A, nitermax, epsilon):
        self.A = A
        self.x = np.random.random(len(A))
        self.wkpp = None
        self.leigval = None
        self.nitermax = nitermax
        self.iter = 0
        self.epsilon = epsilon
        self.choice = None
        #self.choice = int(input(
            #"Nous utilisons les décompositions pour calculer la plus petite valeur propre.\n1 - Décomposition de Cholesky\n2 - Décomposition LU\n3 - Décomposition QR\nLaquelle chosissez vous (numéro en réponse)?"))
        self.cholesky = md.Cholesky(self.A)
        self.lu = md.LU(self.A)
        self.qr = md.QR(self.A)

    def inversed_power_method(self):
        k = 0

        while self.iter < self.nitermax:
            self.iter += 1
            if k == 0:
                wk = self.x / np.linalg.norm(self.x)
            else:
                wk = self.wkpp

            if self.choice == "Cholesky":
                mat_1 = self.cholesky.decomposition()[0]
                mat_2 = self.cholesky.decomposition()[1]
            elif self.choice == "LU":
                mat_1 = self.lu.decomposition()[0]
                mat_2 = self.lu.decomposition()[1]
            elif self.choice == "QR":
                mat_1 = self.qr.decomposition()[0]
                mat_2 = self.qr.decomposition()[1]

            y_int = np.linalg.solve(mat_1, wk)
            ck = np.linalg.solve(mat_2, y_int)
            self.wkpp = ck / np.linalg.norm(ck)

            if self.wkpp is not None:
                self.diff = np.linalg.norm(self.wkpp - wk)

                if self.diff <= self.epsilon:
                    break

            self.leigval = 1 / np.linalg.norm(ck)
            k += 1

        return k, self.wkpp, self.leigval, self.diff


###

"""A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
x = np.array([[1], [1], [1]])
test = InversedPower(A, nitermax=150, epsilon=10 ** (-17))
print("k =", test.inversed_power_method()[0])
print("approximation vecteur propre =", test.inversed_power_method()[1])
print("plus petite valeur propre", test.inversed_power_method()[2])
print("difference =", test.inversed_power_method()[3])
"""
###
