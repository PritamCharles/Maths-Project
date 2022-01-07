import src.gui.main_win as mw
import src.gui.iterpow_win as ipw
import src.gui.invpow_win as inpw
import src.gui.euclidnorm_win as enw
import src.gui.cond_win as cw
import src.gui.qrdiag_win as qrd
import src.maths.utils.create_matrix as cm
import src.maths.iterated_power as ip
import src.maths.inversed_power as inp
import src.maths.euclidian_norm as en
import src.maths.conditioning as c
import tkinter as tk
import numpy as np


class Interface:
    def __init__(self):
        self.main_win = mw.MainWindow()
        self.iterpow_win = ipw.IteratedPowerWindow()
        self.invpow_win = inpw.InversedPowerWindow()
        self.euclidnorm_win = enw.EuclidianNormWindow()
        self.qrdiag_win = qrd.QRDiagonalizationWindow()
        self.cond_win = cw.ConditioningWindow()

    def previous_win_method(self):
        if self.main_win.combo1_value == "Puissance itérée":
            root2.withdraw()
            root1.deiconify()
        elif self.main_win.combo1_value == "Puissance inverse":
            root3.withdraw()
            root1.deiconify()
        elif self.main_win.combo1_value == "Norme matricielle euclidienne":
            root4.withdraw()
            root1.deiconify()
        elif self.main_win.combo1_value == "Conditionnement":
            root5.withdraw()
            root1.deiconify()
        elif self.main_win.combo1_value == "Diagonalisation QR":
            root6.withdraw()
            root1.deiconify()

    def display_iterpow_win(self):
        global root2

        root2 = tk.Toplevel()
        self.iterpow_win.display(root2,self.previous_win_method)
        root2.mainloop()

    def display_invpow_win(self):
        global root3

        root3 = tk.Toplevel()
        self.invpow_win.display(root3, self.previous_win_method)
        root3.mainloop()

    def display_euclidnorm_win(self):
        global root4

        root4 = tk.Toplevel()
        self.euclidnorm_win.display(root4, self.previous_win_method)
        root4.mainloop()

    def display_cond_win(self):
        global root5

        root5 = tk.Toplevel()
        self.cond_win.display(root5, self.previous_win_method)
        root5.mainloop()

    def display_qrdiag_win(self):
        global root6

        root6 = tk.Toplevel()
        self.qrdiag_win.display(root6, self.previous_win_method)
        root6.mainloop()

    def mw_butt_action(self):
        global list

        self.main_win.combo1_value = self.main_win.combo1.get()
        self.main_win.combo2_value = self.main_win.combo2.get()
        self.main_win.entry1_value = int(self.main_win.entry1.get())
        self.main_win.entry2_value = float(self.main_win.entry2.get())

        if self.main_win.combo2_value == "Aléatoire":
            self.main_win.array_size_value = int(self.main_win.array_size_entry.get())
            self.get_matrix = cm.Matrix(self.main_win.array_size_value)
            self.main_win.array_values_value = self.get_matrix.random_matrix()

        elif self.main_win.combo2_value == "Personnalisée":
            self.main_win.array_values_value = self.main_win.array_values_entry.get()
            self.main_win.array_values_value = eval(self.main_win.array_values_value.split()[0])

        elif self.main_win.combo2_value == "Aléatoire à coeffs entiers":
            self.main_win.array_size_value = int(self.main_win.array_size_entry.get())
            self.get_matrix = cm.Matrix(self.main_win.array_size_value)
            self.main_win.array_values_value = self.get_matrix.int_random_matrix()

        elif self.main_win.combo2_value == "Matrice de Hilbert":
            self.main_win.array_size_value = int(self.main_win.array_size_entry.get())
            self.get_matrix = cm.Matrix(self.main_win.array_size_value)
            self.main_win.array_values_value = self.get_matrix.hilbert_matrix()

        list = [self.main_win.combo1_value, self.main_win.combo2_value, self.main_win.entry1_value, self.main_win.entry2_value, self.main_win.array_size_value, self.main_win.array_values_value]

        if self.main_win.combo1_value == "Puissance itérée":
            self.iter_pow = ip.IteratedPower(A=list[-1], nitermax=list[2], epsilon=list[3])
            self.iterpow_win.combo2_value = list[1]
            self.iterpow_win.entry1_value = list[2]
            self.iterpow_win.entry2_value = list[3]
            self.iterpow_win.array_size_value = list[4]
            self.iterpow_win.array_value = list[-1]

            nbiter, heigvec, heigval, fepsilon = self.iter_pow.iterated_power_method()
            self.iterpow_win.nbiter = nbiter
            self.iterpow_win.heigvec = heigvec
            self.iterpow_win.heigval = heigval
            self.iterpow_win.fepsilon = fepsilon

            root1.withdraw()
            self.display_iterpow_win()

        elif self.main_win.combo1_value == "Puissance inverse":
            self.main_win.combo_invm_value = self.main_win.combo_invm.get()
            if self.main_win.combo_invm_value == "Cholesky":
                self.invpow_win.combo_invm_value = self.main_win.combo_invm_value
            elif self.main_win.combo_invm_value == "LU":
                self.invpow_win.combo_invm_value = self.main_win.combo_invm_value
            elif self.main_win.combo_invm_value == "QR":
                self.invpow_win.combo_invm_value = self.main_win.combo_invm_value

            self.inv_pow = inp.InversedPower(A=list[-1], nitermax=list[2], epsilon=list[3])
            self.invpow_win.combo2_value = list[1]
            self.invpow_win.entry1_value = list[2]
            self.invpow_win.entry2_value = list[3]
            self.invpow_win.array_size_value = list[4]
            self.invpow_win.array_value = list[-1]

            self.inv_pow.choice = self.main_win.combo_invm.get()
            nbiter, leigvec, leigval, fepsilon = self.inv_pow.inversed_power_method()
            self.invpow_win.nbiter = nbiter
            self.invpow_win.leigvec = leigvec
            self.invpow_win.leigval = leigval
            self.invpow_win.fepsilon = fepsilon

            root1.withdraw()
            self.display_invpow_win()

        if self.main_win.combo1_value == "Norme matricielle euclidienne":
            self.euclidnorm = en.EuclidianNorm(mat=list[-1], nitermax=list[2], epsilon=list[3])
            self.euclidnorm_win.combo2_value = list[1]
            self.euclidnorm_win.entry1_value = list[2]
            self.euclidnorm_win.entry2_value = list[3]
            self.euclidnorm_win.array_size_value = list[4]
            self.euclidnorm_win.array_value = list[-1]
            self.euclidnorm_win.norm_iterpow = self.euclidnorm.mat_norm_iterpow()
            self.euclidnorm_win.norm_numpy = self.euclidnorm.mat_norm_numpy(list[-1])
            self.euclidnorm_win.norm_error = (np.abs(self.euclidnorm_win.norm_numpy - self.euclidnorm_win.norm_iterpow) / self.euclidnorm_win.norm_numpy) * 100

            root1.withdraw()
            self.display_euclidnorm_win()

        if self.main_win.combo1_value == "Conditionnement":
            self.inv_pow = inp.InversedPower(A=list[-1], nitermax=list[2], epsilon=list[3])
            self.cond = c.Conditioning(mat=list[-1], nitermax=list[2], epsilon=list[3])
            self.inv_pow.choice = self.main_win.combo_invm.get()
            leigval = self.inv_pow.inversed_power_method()[2]
            self.cond.leigval = leigval ** 2

            self.cond_win.combo2_value = list[1]
            self.cond_win.entry1_value = list[2]
            self.cond_win.entry2_value = list[3]
            self.cond_win.array_size_value = list[4]
            self.cond_win.array_value = list[-1]
            self.cond_win.cond_iter_inv = self.cond.cond_iterinv()
            self.cond_win.cond_numpy = self.cond.cond_numpy(list[-1])
            self.cond_win.cond_error = (np.abs(self.cond_win.cond_numpy - self.cond_win.cond_iter_inv) / self.cond_win.cond_numpy) * 100

            root1.withdraw()
            self.display_cond_win()

        if self.main_win.combo1_value == "Diagonalisation QR":
            self.qrdiag_win.combo2_value = list[1]
            self.qrdiag_win.entry1_value = list[2]
            self.qrdiag_win.entry2_value = list[3]
            self.qrdiag_win.array_size_value = list[4]
            self.qrdiag_win.array_value = list[-1]

            root1.withdraw()
            self.display_qrdiag_win()

    def display_main(self):
        global root1

        root1 = tk.Tk()
        self.main_win.display(root1, self.mw_butt_action)
        root1.mainloop()

main = Interface()
main.display_main()
