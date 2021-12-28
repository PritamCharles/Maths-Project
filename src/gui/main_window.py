import tkinter as tk
from tkinter import ttk
import src.gui.utils.window as w
import src.gui.utils.menu_bar as mb


class MainWindow:
    def __init__(self):
        self.win = w.Window()
        self.menu_bar = mb.MenuBar()
        self.combo1 = None
        self.combo_invm = None
        self.combo_invm_value = None
        self.combo1_value = None
        self.combo2_value = None
        self.combo2 = None
        self.entry1_value = None
        self.entry1 = None
        self.entry2_value = None
        self.entry2 = None
        self.array_size_value = None
        self.array_size_entry = None
        self.array_values_value = None
        self.array_values_entry = None

    def title_canvas(self, root, canvas):
        canvas.create_text(self.win.size(root)[1] / 13, self.win.size(root)[0] / 25,
                           text="Projet d'algèbre linéaire", font=("segoe script", 10), fill="white")

    def choice_combobox(self, root):
        global temp_can1

        frame1 = tk.Frame(root, bg="#656566", bd=4, relief="groove")
        temp_can1 = tk.Canvas(frame1, bg="#656566", highlightthickness=0)
        tk.Label(temp_can1, text="Choisissez une méthode", font=("Comic Sans MS", 16), bg="#656566", fg="white").grid(row=1, column=1)

        m_list = ["Puissance itérée", "Puissance inverse"]
        self.combo1 = ttk.Combobox(temp_can1, values=m_list, state=False)
        self.combo1.set("Méthode ...")
        self.combo1.config(state="readonly")
        self.combo1.current(0)
        self.combo1.grid(row=2, column=1, pady=(0, 10))

        temp_can1.grid(row=1, column=1)
        frame1.place(x=self.win.size(root)[1] / 4.47, y=self.win.size(root)[0] / 10)

    def choice_parameters(self, root):
        global frame2

        frame2 = tk.Frame(root, bg="#656566", bd=4, relief="groove")

        tk.Label(frame2, text="Type de matrice", font=("Comic Sans MS", 16), bg="#656566", fg="white").grid(row=1, column=1, padx=10)
        tk.Label(frame2, text="Nombre d'itérations", font=("Comic Sans MS", 16), bg="#656566", fg="white").grid(row=1, column=2, padx=10)
        tk.Label(frame2, text="Epsilon", font=("Comic Sans MS", 16), bg="#656566", fg="white").grid(row=1, column=3, padx=10)

        clist = ["Personnalisée", "Aléatoire","Aléatoire à coeffs entiers", "Matrice de Hilbert"]
        self.combo2 = ttk.Combobox(frame2, values=clist)
        self.combo2.config(state="readonly")
        self.combo2.current(0)
        value1 = tk.IntVar(frame2)
        value1.set(100)
        value2 = tk.IntVar(frame2)
        value2.set(10 ** (-15))
        self.entry1 = tk.Entry(frame2, textvariable=value1)
        self.entry2 = tk.Entry(frame2, textvariable=value2)

        self.combo2.grid(row=2, column=1, padx=40, pady=10)
        self.entry1.grid(row=2, column=2, padx=40, pady=10)
        self.entry2.grid(row=2, column=3, padx=40, pady=10)

        frame2.place(x=self.win.size(root)[1] / 13.25, y=self.win.size(root)[0] / 3.25)

    def array_button_action(self):
        self.combo1_value = self.combo1.get()
        self.combo2_value = self.combo2.get()
        temp_frame = tk.Frame(frame2, bg="#656566")
        temp_can2 = tk.Canvas(temp_frame, bg="#656566", highlightthickness=0)
        temp_can2.delete("all")

        lsrm_list = ["LU", "Cholesky", "QR"]
        if self.combo1_value == "Puissance inverse":
            tk.Label(temp_can1, text="Méthode de résolution", font=("Comic Sans MS", 12), bg="#656566", fg="white").grid(row=3, column=1)
            self.combo_invm = ttk.Combobox(temp_can1, values=lsrm_list, state=False)
            self.combo_invm.set("Méth. de résolution ...")
            self.combo_invm.config(state="readonly")
            self.combo_invm.current(0)
            self.combo_invm.grid(row=4, column=1)

        if (self.combo2_value == "Aléatoire") or (self.combo2_value == "Aléatoire à coeffs entiers") or (self.combo2_value == "Matrice de Hilbert"):
            tk.Label(temp_can2, text="Taille de la matrice", font=("Comic Sans MS", 16), bg="#656566", fg="white").grid(row=3, column=1, padx=10)
            array_size_value = tk.IntVar(temp_can2)
            array_size_value.set(3)
            self.array_size_entry = tk.Entry(temp_can2, textvariable=array_size_value)
            self.array_size_entry.grid(row=4, column=1, padx=40, pady=10)

        elif self.combo2_value == "Personnalisée":
            tk.Label(temp_can2, text="Matrice", font=("Comic Sans MS", 16), bg="#656566", fg="white").grid(row=3, column=1, padx=10)
            array_values = tk.StringVar(temp_can2)
            self.array_values_entry = tk.Entry(temp_can2, textvariable=array_values)
            self.array_values_entry.insert(0, "[[3,1,1],[1,3,1],[1,1,3]]")
            self.array_values_entry.grid(row=4, column=1, padx=40, pady=10)

        temp_can2.grid(row=3, column=1)
        temp_frame.grid(row=3, column=1)

    def buttons(self, root, func):
        tk.Button(frame2, text="Choose array parameters", bg="#070B4E", font=("Cambria", 12), fg="white", relief="ridge", command=self.array_button_action).grid(row=3, column=2, padx=40, pady=5)
        tk.Button(frame2, text="RUN", bg="#070B4E", font=("Cambria", 16), fg="white", relief="ridge", command=func).grid(row=3, column=3, pady=(0, 3))
        tk.Button(root, text="Quitter", bg="#2F2F40", font=20, fg="white", relief="ridge", bd=8, command=root.destroy).place(x=self.win.size(root)[1] / 1.75, y=self.win.size(root)[0] / 1.75)

    def display(self, root, func):
        root.resizable(False, False)
        can = tk.Canvas(root, width=int(self.win.size(root)[1] / 1.5), height=int(self.win.size(root)[0] / 1.5), bg="black")
        self.win.set_window(root, height=int(self.win.size(root)[1] / 1.5),
                               width=int(self.win.size(root)[0] / 1.5),
                               anchorx=int(self.win.size(root)[1] / 2.25 - (self.win.size(root)[1] / 3.75)),
                               anchory=int(self.win.size(root)[0] / 2.25 - (self.win.size(root)[0] / 3.75)))
        self.menu_bar.menu_bar(root)
        self.title_canvas(root, can)
        self.choice_combobox(root)
        self.choice_parameters(root)
        self.buttons(root, func)
        can.pack()
