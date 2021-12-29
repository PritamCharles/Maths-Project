import tkinter as tk
import src.gui.utils.window as w
import src.gui.utils.menu_bar as mb

class QRDiagonalizationWindow:
    def __init__(self):
        self.win = w.Window()
        self.menu_bar = mb.MenuBar()
        self.combo2_value = None
        self.entry1_value = None
        self.entry2_value = None
        self.array_size_value = None
        self.array_value = None

    def title_canvas(self, root, canvas):
        canvas.create_text(self.win.size(root)[1] / 8.5, self.win.size(root)[0] / 25,
                           text="Diagonalisation QR", font=("segoe script", 12), fill="white")

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

    def button(self, root, func):
        tk.Button(root, text="Changer les paramètres", bg="#070B4E", font=("Cambria", 12), fg="white", relief="ridge", bd=4, command=func).place(x=self.win.size(root)[1] / 16, y=self.win.size(root)[0] / 1.75)

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
        
    def display(self, root, func):
        root.resizable(False, False)
        can = tk.Canvas(root, width=int(self.win.size(root)[1] / 1.5), height=int(self.win.size(root)[0] / 1.5), bg="black")
        self.win.set_window(root, height=int(self.win.size(root)[1] / 1.5),
                            width=int(self.win.size(root)[0] / 1.5),
                            anchorx=int(self.win.size(root)[1] / 2.25 - (self.win.size(root)[1] / 3.75)),
                            anchory=int(self.win.size(root)[0] / 2.25 - (self.win.size(root)[0] / 3.75)))
        #self.win.set_background(can, "./src/gui/img/mathematics_curves2_wp.png")
        self.menu_bar.menu_bar(root)
        self.title_canvas(root, can)
        self.show_parameters(root)
        self.show_matrix(root)
        self.button(root, func)
        can.pack()
