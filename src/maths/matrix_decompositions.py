import numpy as np
import scipy.linalg


class Cholesky:
    def __init__(self, A):
        self.A = A

    def decomposition(self):
        L = np.linalg.cholesky(self.A)
        Lt = np.transpose(L)

        return L, Lt


class LU:
    def __init__(self, A):
        self.A = A

    def decomposition(self):
        L = scipy.linalg.lu(self.A)[1]
        U = scipy.linalg.lu(self.A)[2]

        return L, U


class QR:
    def __init__(self, A):
        self.A = A

    def decomposition(self):
        Q = np.linalg.qr(self.A)[0]
        R = np.linalg.qr(self.A)[1]

        return Q, R
