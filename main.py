import src.gui.main_window as mw
import src.gui.iterated_power_window as ipw
import src.gui.inversed_power_window as inpw
import src.maths.utils as u
import src.maths.iterated_power as ip
import src.maths.inversed_power as inp
import tkinter as tk


class Interface:
    def __init__(self):
        self.main_win = mw.MainWindow()
        self.iterpow_win = ipw.IteratedPowerWindow()
        self.invpow_win = inpw.InversedPowerWindow()

    def display_iteratedpower_win(self):
        root2 = tk.Toplevel()
        self.iterpow_win.display(root2)
        root2.mainloop()

    def display_inversedpower_win(self):
        root3 = tk.Toplevel()
        self.invpow_win.display(root3)
        root3.mainloop()

    def mw_butt_action(self):
        global list

        self.main_win.combo1_value = self.main_win.combo1.get()
        self.main_win.combo2_value = self.main_win.combo2.get()
        self.main_win.entry1_value = int(self.main_win.entry1.get())
        self.main_win.entry2_value = float(self.main_win.entry2.get())

        if self.main_win.combo2_value == "Aléatoire":
            self.main_win.array_size_value = int(self.main_win.array_size_entry.get())
            self.get_matrix = u.Matrix(self.main_win.array_size_value)
            self.main_win.array_values_value = self.get_matrix.random_matrix()

        elif self.main_win.combo2_value == "Personnalisée":
            self.main_win.array_values_value = self.main_win.array_values_entry.get()
            self.main_win.array_values_value = eval(self.main_win.array_values_value.split()[0])

        elif self.main_win.combo2_value == "Aléatoire à coeffs entiers":
            self.main_win.array_size_value = int(self.main_win.array_size_entry.get())
            self.get_matrix = u.Matrix(self.main_win.array_size_value)
            self.main_win.array_values_value = self.get_matrix.int_random_matrix()

        elif self.main_win.combo2_value == "Matrice de Hilbert":
            self.main_win.array_size_value = int(self.main_win.array_size_entry.get())
            self.get_matrix = u.Matrix(self.main_win.array_size_value)
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
            self.display_iteratedpower_win()

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
            self.display_inversedpower_win()

    def display(self):
        global root1

        root1 = tk.Tk()
        self.main_win.display(root1, self.mw_butt_action)
        root1.mainloop()

main = Interface()
#main.display_iteratedpower_win()
main.display()
