import tkinter as tk

class Aplication:
    cont = 0

    def __init__(self, master=None):
        # Frame() é a janela top-levep da interface
        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        # widget1 é o container pai do rótulo
        self.msg = tk.Label(self.widget1, text='Hello World!')
        self.msg['font'] = ('Verdana', '25', 'italic', 'bold')
        self.msg.pack(side=tk.TOP)

        # widget1 é o container pai do botão
        self.sair = tk.Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '12', 'bold')
        self.sair['bg'] = 'red'
        self.sair['width'] = 15
        self.sair['height'] = 1
        self.sair['command'] = self.widget1.quit
        self.sair.pack(side=tk.RIGHT)

        # widget1 é o container pai do botão
        self.btn = tk.Button(self.widget1)
        self.btn['text'] = 'Click me'
        self.btn['font'] = ('Calibri', '12')
        self.btn['width'] = 15
        # Adicionando um event handler ao botão
        self.btn.bind("<Button-1>", self.mudar_texto)
        self.btn.pack(side=tk.LEFT)

        """
            width – Largura do widget;
            height – Altura do widget;
            text – Texto a ser exibido no widget;
            font – Família da fonte do texto;
            fg – Cor do texto do widget;
            bg – Cor de fundo do widget;
            side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).
        """

    def mudar_texto(self, event):
        self.cont += 1
        if self.cont == 1:
            self.msg['text'] = f'O botão recebeu {self.cont} clique'
        else:
            self.msg['text'] = f'O botão recebeu {self.cont} cliques'


if __name__ == '__main__':
    root = tk.Tk()
    Aplication(root)
    root.mainloop()
