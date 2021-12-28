import tkinter as tk
import src.gui.utils.window as w
import src.gui.utils.menu_bar as mb
import src.gui.main_window as mw


class InversedPowerWindow:
    def __init__(self):
        self.win = w.Window()
        self.menu_bar = mb.MenuBar()
        self.main_win = mw.MainWindow()
        self.combo2_value = None
        self.combo_inv_value = None
        self.entry1_value = None
        self.entry2_value = None
        self.array_size_value = None
        self.array_value = None
        self.nbiter = None
        self.leigvec = None
        self.leigval = None
        self.fepsilon = None

    def title_canvas(self, root, canvas):
        canvas.create_text(self.win.size(root)[1] / 8.5, self.win.size(root)[0] / 25,
                           text="Méthode de la puissance inverse", font=("segoe script", 12), fill="white")

    def show_parameters(self, root):
        frame1 = tk.Frame(root, bg="#2F2F40", bd=4, relief="groove")

        tk.Label(frame1, text="Paramètres choisis:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=1, column=1)
        tk.Label(frame1, text="Type matrice:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=2, column=1)
        tk.Label(frame1, text="Méth. résol:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=3, column=1)
        tk.Label(frame1, text="Nb iter max:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=4, column=1)
        tk.Label(frame1, text="Epsilon", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=5, column=1)

        tk.Label(frame1, text=str(self.combo2_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=2, column=2)
        tk.Label(frame1, text=str(self.combo_inv_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=3, column=2)
        tk.Label(frame1, text=str(self.entry1_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=4, column=2)
        tk.Label(frame1, text=str(self.entry2_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=5, column=2)

        frame1.place(x=self.win.size(root)[1] / 140, y=self.win.size(root)[0] / 14)

    def show_matrix(self, root):
        frame2 = tk.Frame(root, bg="#2F2F40")
        tk.Label(frame2, text="Matrice d'étude", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=1, column=1, pady=10)

        for i in range(len(self.array_value)):
            if self.array_size_value == 3:
                tk.Label(frame2, text=str(self.array_value[i]), font=("Comic Sans MS", 10), bg="#2F2F40", fg="white").grid(row=i + 2, column=1)
            if self.array_size_value <= 4:
                tk.Label(frame2, text=str(self.array_value[i]), font=("Comic Sans MS", 8), bg="#2F2F40", fg="white").grid(row=i + 2, column=1)
            elif self.array_size_value <= 8:
                tk.Label(frame2, text=str(self.array_value[i]), font=("Comic Sans MS", 6), bg="#2F2F40", fg="white").grid(row=i + 2, column=1)
        if self.array_size_value > 8:
            tk.Label(frame2, text="(Trop grande pour être affichée)", font=("Comic Sans MS", 10), bg="#2F2F40", fg="white").grid(row=2, column=1)
            print("Matrice d'étude:", self.array_value)

        frame2.place(x=self.win.size(root)[1] / 26, y=self.win.size(root)[0] / 4)

    def show_results(self, root):
        frame3 = tk.Frame(root, bg="#2F2F40")
        tk.Label(frame3, text="Nb d'itérations", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=1, column=1, pady=(0, 10))
        tk.Label(frame3, text="Vecteur propre de la plus petite valeur propre", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=3, column=1, pady=(0, 10))
        tk.Label(frame3, text="Plus petite valeur propre", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=5, column=1, pady=(0, 10))
        tk.Label(frame3, text="Diff ||wk - wk-1||", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=7, column=1, pady=(0, 10))

        tk.Label(frame3, text=str(self.nbiter), font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=2, column=1, pady=(0, 40))

        if self.array_size_value <= 5:
            tk.Label(frame3, text=str(self.leigvec), font=("Comic Sans MS", 10), bg="#2F2F40", fg="white").grid(row=4, column=1, pady=(0, 40))
        else:
            tk.Label(frame3, text="(Trop grand pour être affiché)", font=("Comic Sans MS", 10), bg="#2F2F40", fg="white").grid(row=4, column=1, pady=(0, 40))
            print("Vecteur propre de la plus petite valeur propre:", self.leigvec)

        tk.Label(frame3, text=str(self.leigval), font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=6, column=1, pady=(0, 40))
        tk.Label(frame3, text=str(self.fepsilon), font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=8, column=1, pady=(0, 40))

        frame3.place(x=self.win.size(root)[1] / 3.25, y=self.win.size(root)[0] / 26)

    def display(self, root):
        root.resizable(False, False)
        can = tk.Canvas(root, width=int(self.win.size(root)[1] / 1.5), height=int(self.win.size(root)[0] / 1.5), bg="#2F2F40")
        self.win.set_window(root, height=int(self.win.size(root)[1] / 1.5),
                               width=int(self.win.size(root)[0] / 1.5),
                               anchorx=int(self.win.size(root)[1] / 2.25 - (self.win.size(root)[1] / 3.75)),
                               anchory=int(self.win.size(root)[0] / 2.25 - (self.win.size(root)[0] / 3.75)))
        self.menu_bar.menu_bar(root)
        self.title_canvas(root, can)
        self.show_parameters(root)
        self.show_matrix(root)
        self.show_results(root)
        can.pack()
