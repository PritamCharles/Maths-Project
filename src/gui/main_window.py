import tkinter as tk
from tkinter import ttk
import src.gui.utils.window as w


class MainWindow:
    def __init__(self):
        self.window = w.Window()

    def title_canvas(self, root, canvas):
        canvas.create_text(self.window.size(root)[1] / 9, self.window.size(root)[0] / 18,
                           text="Projet d'algèbre linéaire ", font=("segoe script", 14), fill="black")

    def choice_combobox(self, root):
        frame = tk.Frame(root)
        clist = ["Puissance itérée"]
        combo = ttk.Combobox(frame, values=clist)
        combo.set("Méthode ...")
        combo.pack()
        lab = tk.Label(root, text="Choisissez une méthode", font=("Comic Sans MS", 16)).place(
            x=self.window.size(root)[1] / 4.25, y=self.window.size(root)[0] / 4.5)
        frame.place(x=self.window.size(root)[1] / 3.75, y=self.window.size(root)[0] / 3.5)

    def display(self, root):
        root.resizable(False, False)
        can = tk.Canvas(root, width=int(self.window.size(root)[1] / 1.5), height=int(self.window.size(root)[0] / 1.5))
        self.window.set_window(root, height=int(self.window.size(root)[1] / 1.5),
                               width=int(self.window.size(root)[0] / 1.5),
                               anchorx=int(self.window.size(root)[1] / 2.25 - (self.window.size(root)[1] / 3.75)),
                               anchory=int(self.window.size(root)[0] / 2.25 - (self.window.size(root)[0] / 3.75)))
        self.choice_combobox(root)
        self.title_canvas(root, can)
        can.pack()
        root.mainloop()
