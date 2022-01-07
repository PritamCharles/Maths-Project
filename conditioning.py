import iterated_power as ip
import inversed_power as inp
import utils.create_matrix as cm
import numpy as np


class Conditioning:
    def __init__(self, mat, itermax, epsilon):
        self.iterpow = ip.IteratedPower(mat, itermax, epsilon)
        self.invpow = inp.InversedPower(mat, itermax, epsilon)
        self.heigval = self.iterpow.iterated_power_method()[2]
        self.leigval = self.invpow.inversed_power_method()[2]

    def cond(self):
        return self.heigval / self.leigval

###

matrix = cm.Matrix(size=3)
A = matrix.int_random_matrix()
# A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.random.randint(100, size=(3, 3))
cond = Conditioning(A, itermax=100, epsilon=10 ** (-16))
print("A:", A)
print("cond with iterated and inversed power methods =", cond.cond())
print("cond with numpy =", np.linalg.cond(A))

###