import src.gui.utils.window as w
import src.gui.utils.menu_bar as mb
import tkinter as tk
from PIL import Image

class NormChartWindow:
    def __init__(self):
        self.win = w.Window()
        self.menu_bar = mb.MenuBar()

    def show_image(self, canvas):
        img = Image.open("./src/gui/img/norm_error_chart.png")
        resized_img = img.resize((750, 450))
        resized_img.save("./src/gui/img/norm_error_chart_resized.png")
        img2 = tk.PhotoImage(file="./src/gui/img/norm_error_chart_resized.png")
        canvas.create_image(750 / 1.75, 450 / 1.85, image=img2)
        canvas.image = img2
        canvas.pack()

    def button(self, root, func):
        tk.Button(root, text="Retour", bg="#070B4E", font=("Cambria", 7), fg="white", relief="ridge", bd=4, command=func).place(x=self.win.size(root)[1] / 16, y=self.win.size(root)[0] / 1.75)

    def display(self, root, func):
        root.resizable(False, False)
        can = tk.Canvas(root, width=int(self.win.size(root)[1] / 1.5), height=int(self.win.size(root)[0] / 1.5), bg="black")
        self.win.set_window(root, height=int(self.win.size(root)[1] / 1.5),
                            width=int(self.win.size(root)[0] / 1.5),
                            anchorx=int(self.win.size(root)[1] / 2.25 - (self.win.size(root)[1] / 3.75)),
                            anchory=int(self.win.size(root)[0] / 2.25 - (self.win.size(root)[0] / 3.75)))
        self.show_image(can)
        self.menu_bar.menu_bar(root)
        self.button(root, func)
        can.pack()
