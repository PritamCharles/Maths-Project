import numpy as np
import src.maths.matrix_decompositions as dm


class InversedPower:
    def __init__(self, A, itermax, epsilon):
        self.A = A
        self.x = np.random.random(len(A))
        self.itermax = itermax
        self.iter = 0
        self.epsilon = epsilon
        self.cholesky = dm.Cholesky(self.A)
        self.lu = dm.LU(self.A)
        self.qr = dm.QR(self.A)

    def inversed_power_method(self):
        answ = int(input("Nous utilisons les décompositions pour calculer la plus petite valeur propre.\n1 - Décomposition de Cholesky\n2 - Décomposition LU\n3 - Décomposition QR\nLaquelle chosissez vous (numéro en réponse)?"))
        k = 0

        while self.iter < self.itermax:
            self.iter += 1
            if k == 0:
                wk = self.x / np.linalg.norm(self.x)
            else:
                wk = wkpp

            if answ == 1:
                mat_1 = self.cholesky.decomposition()[0]
                mat_2 = self.cholesky.decomposition()[1]
            elif answ == 2:
                mat_1 = self.lu.decomposition()[0]
                mat_2 = self.lu.decomposition()[1]
            elif answ == 3:
                mat_1 = self.qr.decomposition()[0]
                mat_2 = self.qr.decomposition()[1]

            y_int = np.linalg.solve(mat_1, wk)
            ck = np.linalg.solve(mat_2, y_int)
            wkpp = ck / np.linalg.norm(ck)

            if wkpp is not None:
                self.diff = np.linalg.norm(wkpp - wk)

                if self.diff <= self.epsilon:
                    break

            k += 1
            print("k =", k)
            print("wkpp (approximation valeur propre) =", wkpp)
            print("c =", 1 / np.linalg.norm(ck))
            print("difference =", self.diff)


A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
x = np.array([[1], [1], [1]])
test = InversedPower(A, itermax=100, epsilon=10 ** (-17))
test.inversed_power_method()
