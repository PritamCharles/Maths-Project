import src.gui.utils.window as w
import src.gui.utils.menu_bar as mb
import src.gui.normchart_win as ncw
import tkinter as tk


class EuclidianNormWindow:
    def __init__(self):
        self.win = w.Window()
        self.menu_bar = mb.MenuBar()
        self.combo2_value = None
        self.entry1_value = None
        self.entry2_value = None
        self.array_size_value = None
        self.array_value = None
        self.norm_iterpow = None
        self.norm_numpy = None
        self.norm_error = None

    def title_canvas(self, root, canvas):
        canvas.create_text(self.win.size(root)[1] / 8.5, self.win.size(root)[0] / 25,
                           text="Norme matricielle euclidienne", font=("segoe script", 12), fill="white")

    def show_parameters(self, root):
        frame1 = tk.Frame(root, bg="#2F2F40", bd=4, relief="groove")

        tk.Label(frame1, text="Paramètres choisis:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=1, column=1)
        tk.Label(frame1, text="Type matrice:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=2, column=1)
        tk.Label(frame1, text="Nb iter max:", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=3, column=1)
        tk.Label(frame1, text="Epsilon", font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=4, column=1)

        tk.Label(frame1, text=str(self.combo2_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=2, column=2)
        tk.Label(frame1, text=str(self.entry1_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=3, column=2)
        tk.Label(frame1, text=str(self.entry2_value), font=("Comic Sans MS", 7), bg="#2F2F40", fg="white").grid(row=4, column=2)

        frame1.place(x=self.win.size(root)[1] / 140, y=self.win.size(root)[0] / 14)

    def show_matrix(self, root):
        frame2 = tk.Frame(root, bg="#2F2F40", bd=4, relief="groove")
        tk.Label(frame2, text="Matrice d'étude", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=1, column=1, padx=5, pady=5)

        if self.combo2_value == "Personnalisée":
            for i in range(len(self.array_value)):
                tk.Label(frame2, text=str(self.array_value[i]), font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=i + 2, column=1)

        if (self.combo2_value == "Aléatoire") or (self.combo2_value == "Aléatoire à coeffs entiers") or (self.combo2_value == "Matrice de Hilbert"):
            for i in range(len(self.array_value)):
                if self.array_size_value == 3:
                    tk.Label(frame2, text=str(self.array_value[i]), font=("Comic Sans MS", 10), bg="#2F2F40", fg="white").grid(row=i + 2, column=1)
                if (self.array_size_value >= 4) and (self.array_size_value < 6):
                    tk.Label(frame2, text=str(self.array_value[i]), font=("Comic Sans MS", 8), bg="#2F2F40", fg="white").grid(row=i + 2, column=1)

        frame2.place(x=self.win.size(root)[1] / 140, y=self.win.size(root)[0] / 4)

    def show_results(self, root):
        frame3 = tk.Frame(root, bg="#2F2F40", bd=4, relief="groove")
        tk.Label(frame3, text="Norme matricielle euclidienne - Puissance itérée", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=1, column=1, pady=(0, 10))
        tk.Label(frame3, text="Norme matricielle euclidienne - Numpy", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=3, column=1, pady=(0, 10))
        tk.Label(frame3, text="Erreur relative (en %)", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=5, column=1, pady=(0, 10))

        tk.Label(frame3, text=str(self.norm_iterpow), font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=2, column=1, pady=(0, 40))
        tk.Label(frame3, text=str(self.norm_numpy), font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=4, column=1, pady=(0, 50))
        tk.Label(frame3, text=str(round(self.norm_error, 2)) + " %", font=("Comic Sans MS", 12), bg="#2F2F40", fg="white").grid(row=6, column=1)

        frame3.place(x=self.win.size(root)[1] / 3.25, y=self.win.size(root)[0] / 26)

    def show_plot(self):
        root_bis = tk.Toplevel()

        def func():
            root_bis.withdraw()

        self.chartwin = ncw.NormChartWindow()
        self.chartwin.display(root_bis, func)

    def button(self, root, func1):
        tk.Button(root, text="Changer les paramètres", bg="#070B4E", font=("Cambria", 12), fg="white", relief="ridge", bd=4, command=func1).place(x=self.win.size(root)[1] / 16, y=self.win.size(root)[0] / 1.75)
        tk.Button(root, text="Essais sur des matrices plus grandes", bg="#070B4E", font=("Cambria", 10), fg="white", relief="ridge", bd=4, command=self.show_plot).place(x=self.win.size(root)[1] / 16, y=self.win.size(root)[0] / 2)

    def display(self, root, func1):
        root.resizable(False, False)
        can = tk.Canvas(root, width=int(self.win.size(root)[1] / 1.5), height=int(self.win.size(root)[0] / 1.5),
                        bg="black")
        self.win.set_window(root, height=int(self.win.size(root)[1] / 1.5),
                            width=int(self.win.size(root)[0] / 1.5),
                            anchorx=int(self.win.size(root)[1] / 2.25 - (self.win.size(root)[1] / 3.75)),
                            anchory=int(self.win.size(root)[0] / 2.25 - (self.win.size(root)[0] / 3.75)))
        self.win.set_background(can, "./src/gui/img/mathematics_curves4_wp.gif")
        self.menu_bar.menu_bar(root)
        self.title_canvas(root, can)
        self.show_parameters(root)
        self.show_matrix(root)
        self.show_results(root)
        self.button(root, func1)
        can.pack()
