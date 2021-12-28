import tkinter as tk

class MenuBar:
    def m_bar(self):
        wmb = tk.Toplevel()
        wmb.title("Remerciements")
        wmb.geometry("700x400")
        wmb.minsize(300, 300)
        wmb.config(background="#2F2F40")
        can = tk.Canvas(wmb, height=400, width=700, bg="#2F2F40", highlightthickness=0)


    def menu_bar(self, root):
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="A propos", command=self.m_bar)
        file_menu.add_command(label="Quitter l'application", command=root.destroy)
        menu_bar.add_cascade(label=" Aide", menu=file_menu)

        root.config(menu=menu_bar)
