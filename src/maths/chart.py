import src.maths.euclidian_norm as en
import src.maths.conditioning as c
import src.maths.inversed_power as inp
import src.maths.utils.charts_utils as cu
import src.maths.utils.create_matrix as cm
import numpy as np

class NormValues:
    def xvalues(self):
        return [i for i in range(3, 1003, 50)]

    def yvalues_random(self):
        lyaxis_random = []
        for i in self.xvalues():
            self.matrix = cm.Matrix(i)
            mat = self.matrix.random_matrix()
            self.euclidnorm = en.EuclidianNorm(mat, nitermax=100, epsilon=10 ** (-16))
            mat_norm_numpy = self.euclidnorm.mat_norm_numpy(mat)
            mat_norm_iterpow = self.euclidnorm.mat_norm_iterpow()
            error = round((np.abs(mat_norm_numpy - mat_norm_iterpow) / mat_norm_numpy) * 100, 2)
            lyaxis_random.append(error)
        return lyaxis_random

    def yvalues_int(self):
        lyaxis_int = []
        for i in self.xvalues():
            self.matrix = cm.Matrix(i)
            mat = self.matrix.int_random_matrix()
            self.euclidnorm = en.EuclidianNorm(mat, nitermax=100, epsilon=10 ** (-16))
            mat_norm_numpy = self.euclidnorm.mat_norm_numpy(mat)
            mat_norm_iterpow = self.euclidnorm.mat_norm_iterpow()
            error = round((np.abs(mat_norm_numpy - mat_norm_iterpow) / mat_norm_numpy) * 100, 2)
            lyaxis_int.append(error)
        return lyaxis_int

    def yvalues_hilbert(self):
        lyaxis_hilbert = []
        for i in self.xvalues():
            self.matrix = cm.Matrix(i)
            mat = self.matrix.hilbert_matrix()
            self.euclidnorm = en.EuclidianNorm(mat, nitermax=100, epsilon=10 ** (-16))
            mat_norm_numpy = self.euclidnorm.mat_norm_numpy(mat)
            mat_norm_iterpow = self.euclidnorm.mat_norm_iterpow()
            error = round((np.abs(mat_norm_numpy - mat_norm_iterpow) / mat_norm_numpy) * 100, 2)
            lyaxis_hilbert.append(error)
        return lyaxis_hilbert

class CondValues:
    def xvalues(self):
        return [i for i in range(3, 1003, 100)]

    def yvalues_random(self):
        lyaxis_random = []
        for i in self.xvalues():
            self.matrix = cm.Matrix(i)
            mat = self.matrix.random_matrix()
            self.cond = c.Conditioning(mat, nitermax=100, epsilon=10 ** (-16))
            cond_numpy = self.cond.cond_numpy(mat)
            cond_iterinv = self.cond.cond_iterinv()
            error = round((np.abs(cond_numpy - cond_iterinv) / cond_numpy) * 100, 2)
            lyaxis_random.append(error)
        return lyaxis_random

    def yvalues_int(self):
        lyaxis_int = []
        for i in self.xvalues():
            self.matrix = cm.Matrix(i)
            mat = self.matrix.int_random_matrix()
            self.cond = c.Conditioning(mat, nitermax=100, epsilon=10 ** (-16))
            cond_numpy = self.cond.cond_numpy(mat)
            cond_iterinv = self.cond.cond_iterinv()
            error = round((np.abs(cond_numpy - cond_iterinv) / cond_numpy) * 100, 2)
            lyaxis_int.append(error)
        return lyaxis_int

    def yvalues_hilbert(self):
        lyaxis_hilbert = []
        for i in self.xvalues():
            self.matrix = cm.Matrix(i)
            mat = self.matrix.hilbert_matrix()
            self.cond = c.Conditioning(mat, nitermax=100, epsilon=10 ** (-16))
            cond_numpy = self.cond.cond_numpy(mat)
            cond_iterinv = self.cond.cond_iterinv()
            error = round((np.abs(cond_numpy - cond_iterinv) / cond_numpy) * 100, 2)
            lyaxis_hilbert.append(error)
        return lyaxis_hilbert


"""norm = NormValues()
chart = cu.Chart(title="Erreur relative en fonction de la taille de la matrice pour le calcul de la norme matricielle", xlabel="Taille de la matrice", ylabel="Erreur relative (en %)")
nlistx = [norm.xvalues(), norm.xvalues(), norm.xvalues()]
nlisty = [norm.yvalues_random(), norm.yvalues_int(), norm.yvalues_hilbert()]
nlistlabels = ["Matrices aléatoires", "Matrices à coefficients entiers", "Matrices de Hilbert"]
chart.plot(nb_plots=3, list_xvalues=nlistx, list_yvalues=nlisty, list_labels=nlistlabels)

cond = CondValues()
chart = cu.Chart(title="Erreur relative en fonction de la taille de la matrice pour le calcul du conditionnement", xlabel="Taille de la matrice", ylabel="Erreur relative (en %)")
clistx = [cond.xvalues(), cond.xvalues(), cond.xvalues()]
clisty = [cond.yvalues_random(), cond.yvalues_int(), cond.yvalues_hilbert()]
clistlabels = ["Matrices aléatoires", "Matrices à coefficients entiers", "Matrices de Hilbert"]
chart.plot(nb_plots=3, list_xvalues=clistx, list_yvalues=clisty, list_labels=clistlabels)
"""
###

