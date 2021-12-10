import src.gui.main_window as mw
import tkinter as tk


class Interface:
    def __init__(self):
        self.main_window = mw.MainWindow()

    def display(self, root):
        self.main_window.display(root)
        root.mainloop()


root = tk.Tk()
main = Interface()
main.display(root)
