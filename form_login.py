from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "14")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do Usuário")
        self.titulo["font"] = ("Arial", "12", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "10")
        self.autenticar["command"] = self.verify
        self.autenticar.pack()

        self.msg = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.msg.pack()

    # Verificação de Usuário e senha
    def verify(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if usuario == "Victor" and senha == "victor":
            self.msg["text"] = "Autenticado"
        else:
            self.msg["text"] = "Usuário ou senha invalida!"


root = Tk()
Application(root)
root.mainloop()


