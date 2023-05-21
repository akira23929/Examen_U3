from tkinter import *
from menu import *


def main():
    root1 = Tk()
    root1.wm_title("Menu")
    app = Menu(root1)
    app.mainloop()

if __name__ == "__main__":
    main()

class Menu(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, width=230, height=260)
        self.content = Frame(self)  
        self.pack()
        self.create_widgets()

    def fVentana(self):
        from ventana import Ventana
        Ventana()

    def fListado(self):  
        from listado import main
        main()      

    def create_widgets(self):
        frame1 = Frame(self, bg="Turquoise")
        frame1.place(x=0, y=0, width=293, height=259)        
        self.btnVentana = Button(frame1, text="Registros", command=self.fVentana, bg="chocolate", fg="white")
        self.btnVentana.place(x=70, y=50, width=80, height=30)        
        self.btnlistado = Button(frame1, text="Lista", command=self.fListado, bg="chocolate", fg="white")
        self.btnlistado.place(x=70, y=90, width=80,height=30)