from PIL import ImageTk


class Window:
    def set_window(self, root, height, width, anchorx, anchory):
        root.title("Ma313 - Projet d'algèbre numérique linéaire")
        root.geometry(
            "{height}x{width}+{anchorx}+{anchory}".format(height=height, width=width, anchorx=anchorx, anchory=anchory))
        root.minsize(width=int(width / 4), height=int(height / 4))

    def set_background(self, can, path):
        global image

        image = ImageTk.PhotoImage(file=path)
        can.pack(fill="both", expand=True)
        can.create_image(0, 0, image=image, anchorx="nw")

    def size(self, root):
        height = root.winfo_screenheight()
        width = root.winfo_screenwidth()
        return height, width
