import numpy as np
import utils.create_matrix as cm


class IteratedPower:
    def __init__(self, A, nitermax, epsilon):
        self.A = A
        self.x = np.random.random(len(A))
        self.wkpp = None
        self.heigval = None
        self.nitermax = nitermax
        self.iter = 0
        self.epsilon = epsilon
        self.diff = None

    def iterated_power_method(self):
        k = 0

        while self.iter < self.nitermax:
            self.iter += 1
            if k == 0:
                wk = self.x / np.linalg.norm(self.x)
            else:
                wk = self.wkpp

            ck = np.dot(self.A, wk)
            self.wkpp = ck / np.linalg.norm(ck)

            if self.wkpp is not None:
                self.diff = np.linalg.norm(self.wkpp - wk)

                if self.diff <= self.epsilon:
                    break

            self.heigval = np.linalg.norm(ck)
            k += 1

        return k, self.wkpp, self.heigval, self.diff

    def iterated_power_method2(self):
        k = 0

        for i in range(len(self.A)):
            for j in range(len(self.A)):
                if self.A[i, j] < 0:
                    state = False
        state = True

        if not state:
            while self.iter < self.nitermax:
                self.iter += 1
                if k == 0:
                    wk = self.x / np.linalg.norm(self.x)
                    wk_alternate = ((-1) ** k) * wk
                else:
                    wk = self.wkpp
                    wk_alternate = ((-1) ** k) * wk

                ck = np.dot(self.A, wk_alternate)
                self.wkpp = ck / np.linalg.norm(ck)

                if self.wkpp is not None:
                    self.diff = np.linalg.norm(self.wkpp - wk)

                    if self.diff <= self.epsilon:
                        break

                self.heigval = np.linalg.norm(ck)
                k += 1

            return k, self.wkpp, self.heigval, self.diff

        else:
            while self.iter < self.nitermax:
                self.iter += 1
                if k == 0:
                    wk = self.x / np.linalg.norm(self.x)
                else:
                    wk = self.wkpp

                ck = np.dot(self.A, wk)
                self.wkpp = ck / np.linalg.norm(ck)

                if self.wkpp is not None:
                    self.diff = np.linalg.norm(self.wkpp - wk)

                    if self.diff <= self.epsilon:
                        break

                self.heigval = np.linalg.norm(ck)
                k += 1

            return k, self.wkpp, self.heigval, self.diff


###

matrix = cm.Matrix(size=3)
# A = matrix.int_random_matrix()
# A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
A = np.array([[0, 1], [1, 0]])
test = IteratedPower(A, nitermax=100, epsilon=10 ** (-15))
print("A:", A)
print("k =", test.iterated_power_method2()[0])
print("approx vecteur propre =", test.iterated_power_method2()[1])
print("plus grande valeur propre =", test.iterated_power_method2()[2])
print("erreur relative =", test.iterated_power_method2()[3])

###
