import iterated_power as ip
import utils.create_matrix as cm
import numpy as np


class EuclidianNorm:
    def __init__(self, mat, nitermax, epsilon):
        self.temp_mat = np.dot(np.transpose(mat), mat)
        self.iterpow = ip.IteratedPower(self.temp_mat, nitermax, epsilon)
        self.x = self.iterpow.x
        self.eigval = self.iterpow.iterated_power_method()[2]

    def mat_norm_iterpow(self):
        return np.sqrt(self.eigval)

    def mat_norm_numpy(self, mat):
        return np.linalg.norm(mat)

###

matrix = cm.Matrix(size=3)
A = matrix.int_random_matrix()
# A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
# A = np.random.randint(100, size=(1000, 1000))
print("A =", A)
norm = EuclidianNorm(A, nitermax=100, epsilon=10 ** (-16))
print("norm with iterated power method =", norm.mat_norm_iterpow())
print("norm with numpy =", norm.mat_norm_numpy(A))

###