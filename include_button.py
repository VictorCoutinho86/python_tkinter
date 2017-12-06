from tkinter import *


class Application:
    def __init__(self, master=None):
        self.widget2 = Frame(master)
        self.widget2.pack()
        self.msg = Label(self.widget2, text="Segundo Widget")
        self.msg["font"] = ("Verdana", "14", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget2)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudartexto)
        self.sair.pack()

    def mudartexto(self, event):
        if self.msg["text"] == "Segundo Widget":
            self.msg["text"] = "O botão recebeu um clique!"


root = Tk()
Application(root)
root.mainloop()
