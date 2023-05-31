import tkinter as tk

class Application:
    USER = 'WGF'
    PASSWORD = 'LOL'

    def __init__(self, master=None):
        self.fonte_default = ('Times New Roman', '14')

        self.primeiro_container = tk.Frame(master)
        self.primeiro_container['pady'] = 10
        self.primeiro_container.pack()

        self.segundo_container = tk.Frame(master)
        self.segundo_container['padx'] = 20
        self.segundo_container.pack()

        self.terceiro_container = tk.Frame(master)
        self.terceiro_container['padx'] = 20
        self.terceiro_container.pack()

        self.quarto_container = tk.Frame(master)
        self.quarto_container['pady'] = 20
        self.quarto_container.pack()

        self.titulo = tk.Label(self.primeiro_container)
        self.titulo['text'] =  "Dados do usuário"
        self.titulo['font'] = ('Arial', '16', 'bold')
        self.titulo.pack()

        self.nomeLabel = tk.Label(self.segundo_container)
        self.nomeLabel['text'] = 'Nome'
        self.nomeLabel['font'] = self.fonte_default
        self.nomeLabel.pack(side=tk.LEFT)

        self.nomeEntry = tk.Entry(self.segundo_container)
        self.nomeEntry['width'] = 35
        self.nomeEntry['font'] = self.fonte_default
        self.nomeEntry.pack(side=tk.LEFT)

        self.senhaLabel = tk.Label(self.terceiro_container)
        self.senhaLabel['text'] = 'Senha'
        self.senhaLabel['font'] = self.fonte_default
        self.senhaLabel.pack(side=tk.LEFT)

        self.senhaEntry = tk.Entry(self.terceiro_container)
        self.senhaEntry['width'] = 30
        self.senhaEntry['font'] = self.fonte_default
        self.senhaEntry['show'] = '*'
        self.senhaEntry.pack(side=tk.LEFT)

        self.autenticar = tk.Button(self.quarto_container)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '10')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificar_senha
        self.autenticar.pack()

        self.mensagem = tk.Label(self.quarto_container)
        self.mensagem['text'] = ''
        self.mensagem['font'] = ('Arial', '12', 'bold')
        self.mensagem.pack(side=tk.TOP)


    def verificar_senha(self):
        user = self.nomeEntry.get()
        pwd = self.senhaEntry.get()

        if user != self.USER:
            self.mensagem['text'] = 'Usuário incorreto!'
            self.mensagem['fg'] = 'orange'
        elif pwd != self.PASSWORD:
            self.mensagem['text'] = 'Senha incorreta!'
            self.mensagem['fg'] = 'orange'
        else:
            self.mensagem['text'] = 'Autenticado'
            self.mensagem['fg'] = 'green'


if __name__ == '__main__':
    root = tk.Tk()
    Application(root)
    root.mainloop()
