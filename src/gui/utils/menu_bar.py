import tkinter as tk

class MenuBar:
    def menu_bar(self, root):
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Quitter l'application", command=root.destroy)
        menu_bar.add_cascade(label=" Aide", menu=file_menu)

        root.config(menu=menu_bar)
