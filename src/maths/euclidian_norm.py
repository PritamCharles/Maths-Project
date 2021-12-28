import iterated_power as ip
import numpy as np


class EuclidianNorm:
    def __init__(self, mat, itermax, epsilon):
        self.temp_mat = np.dot(np.transpose(mat), mat)
        self.iterpow = ip.IteratedPower(self.temp_mat, itermax, epsilon)
        self.x = self.iterpow.x
        self.eigval = self.iterpow.iterated_power_method()[2]

    """def vect_norm(self):
        return np.sqrt(np.dot(np.transpose(self.x), self.x))

    def mat_norm(self, mat):
        norm_ax = np.sqrt(np.dot(np.transpose(np.dot(mat, self.x)), np.dot(mat, self.x)))
        mat_norm = norm_ax / self.vect_norm()
        return mat_norm

    def norm(self, mat):
        list = []
        for i in range(0, 100):
            self.vect_norm()
            list.append(self.mat_norm(mat))

        return max(list)"""

    def mat_norm(self):
        return np.sqrt(self.eigval)

#A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
A = np.random.randint(100, size=(3, 3))
norm = EuclidianNorm(A, itermax=100, epsilon=10 ** (-16))
print("norm with iterated power method:", norm.mat_norm())
print("norm with numpy:", np.linalg.norm(A))
