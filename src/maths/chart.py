import src.maths.euclidian_norm as en
import src.maths.utils.charts_utils as cu
import numpy as np

class NormValues:
    def random_mat(self, size):
        return np.random.randn(size, size)

    def randomint_mat(self, size):
        return np.random.randint(100, size=(size, size), dtype=int)

    def xvalues(self):
        return [i for i in range(3, 1003, 50)]

    def yvalues_random(self):
        lyaxis_random = []
        for i in self.xvalues():
            self.euclidnorm = en.EuclidianNorm(self.random_mat(i), nitermax=100, epsilon=10 ** (-16))
            mat_norm_numpy = self.euclidnorm.mat_norm_numpy(self.random_mat(i))
            mat_norm_iterpow = self.euclidnorm.mat_norm_iterpow()
            error = round((np.abs(mat_norm_numpy - mat_norm_iterpow) / mat_norm_numpy) * 100, 2)
            lyaxis_random.append(error)
        return lyaxis_random

    def yvalues_int(self):
        lyaxis_int = []
        for i in self.xvalues():
            self.euclidnorm = en.EuclidianNorm(self.randomint_mat(i), nitermax=100, epsilon=10 ** (-16))
            mat_norm_numpy = self.euclidnorm.mat_norm_numpy(self.randomint_mat(i))
            mat_norm_iterpow = self.euclidnorm.mat_norm_iterpow()
            error = round((np.abs(mat_norm_numpy - mat_norm_iterpow) / mat_norm_numpy) * 100, 2)
            lyaxis_int.append(error)
        return lyaxis_int

values = NormValues()
chart = cu.Chart(title="Erreur relative en fonction de la taille de la matrice pour le calcul de la norme matricielle", xlabel="Taille de la matrice", ylabel="Erreur relative (en %)", path="C:/Users/Charles K/Desktop/IPSA/Cours_TD/aero3_moi/Algèbre linéaire numérique/projet/Maths-Project/src/gui/img/norm_error_chart.png")
listx, listy = [values.xvalues(), values.xvalues()], [values.yvalues_random(), values.yvalues_int()]
listlabels = ["Matrices aléatoires", "Matrices à coefficients entiers"]
chart.plot(nb_plots=2, list_xvalues=listx, list_yvalues=listy, list_labels=listlabels)
