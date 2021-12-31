import src.maths.iterated_power as ip
import src.maths.inversed_power as inp
import numpy as np


class Conditioning:
    def __init__(self, mat, nitermax, epsilon):
        self.temp_mat = np.dot(np.transpose(mat), mat)
        self.iterpow = ip.IteratedPower(self.temp_mat, nitermax, epsilon)
        self.invpow = inp.InversedPower(self.temp_mat, nitermax, epsilon)
        self.heigval = self.iterpow.iterated_power_method()[2]
        #self.leigval = self.invpow.inversed_power_method()[2] #(Pour tracer les courbes)
        self.leigval = None

    def cond_iterinv(self):
        return np.sqrt(self.heigval / self.leigval)

    def cond_numpy(self, mat):
        return np.linalg.cond(mat)


"""A = np.array([[3, 1, 1], [1, 3, 1], [1, 1, 3]])
#A = np.random.randint(100, size=(3, 3))
cond = Conditioning(A, nitermax=100, epsilon=10 ** (-16))
print("cond with iterated and inversed power methods:", cond.cond_iterinv())
print("cond with numpy:", np.linalg.cond(A))"""
