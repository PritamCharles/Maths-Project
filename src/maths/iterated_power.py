import numpy as np


class IteratedPower:
    def __init__(self, A, itermax, epsilon):
        self.A = A
        self.x = np.random.random(len(A))
        self.itermax = itermax
        self.iter = 0
        self.epsilon = epsilon
        self.diff = None

    def iterated_power_method(self):
        k = 0

        while self.iter < self.itermax:
            self.iter += 1
            if k == 0:
                wk = self.x / np.linalg.norm(self.x)
            else:
                wk = wkpp

            ck = np.dot(self.A, wk)
            wkpp = ck / np.linalg.norm(ck)

            if wkpp is not None:
                self.diff = np.linalg.norm(wkpp - wk)

                if self.diff <= self.epsilon:
                    break

            k += 1
            print("k =", k)
            print("wkpp (approximation valeur propre) =", wkpp)
            print("c =", np.linalg.norm(ck))
            print("difference =", self.diff)


A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.array([[3, 0, 1], [0, 7, 0], [1, 0, 3]])
x = np.array([[1], [1], [1]])
test = IteratedPower(A, itermax=100, epsilon=10 ** (-17))
test.iterated_power_method()
