from tkinter import *
from tkinter import ttk
import img

janela = Tk()


class Aplicação:
    def __init__(self):
        self.configurarDaTela()
        self.criarFrames()
        self.LabelsEntrys()
        self.criarBotões()
        self.criarTabelaProdutos()
        janela.mainloop()

    def configurarDaTela(self):
        janela.title('Cadastro de Produtos')
        janela.geometry('800x600')
        janela.resizable(True, True)
        janela.minsize(width=760, height=492)
        janela.maxsize(width=900, height=520)
        janela.configure(bg='#F0E68C')

    def criarFrames(self):
        self.topFrame = Frame(janela, bg='#F0E68C', bd=4, highlightbackground='#696969', highlightthickness=3)
        self.topFrame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)

        self.botomFrame = Frame(janela, bg='#F0E68C', bd=3, highlightbackground='#696969', highlightthickness=3)
        self.botomFrame.place(relx=0.01, rely=0.52, relwidth=0.98, relheight=0.47)

    def LabelsEntrys(self):
        self.icone = PhotoImage(file='img/icone2.png')
        self.labelIcone = Label(self.botomFrame, image=self.icone, bg='#F0E68C')
        self.labelIcone.place(relx=0.72, rely=0.02, relwidth=0.28, relheight=0.98)

        self.labelTitulo = Label(self.topFrame, text='MERCADINHO SÃO JOSÉ', font=('bold, aerdana', 18), bg='#F0E68C', fg='#696969')
        self.labelTitulo.place(relx=0.35, rely=0.03)

        self.labelNome = Label(self.topFrame, text='Nome do Produto', bg='#F0E68C', font='bold', fg='#2F4F4F')
        self.labelNome.place(relx=0.05, rely=0.3)
        self.entryNome = Entry(self.topFrame)
        self.entryNome.place(relx=0.05, rely=0.44, relwidth=0.45)

        self.labelQuantidade = Label(self.topFrame, text='Quantidade no Estoque', bg='#F0E68C', font='bold', fg='#2F4F4F')
        self.labelQuantidade.place(relx=0.05, rely=0.55)
        self.entryQuantidade = Entry(self.topFrame)
        self.entryQuantidade.place(relx=0.12, rely=0.68, relwidth=0.07)

        self.labelPreço = Label(self.topFrame, text='Preço Unitário', bg='#F0E68C', font='bold', fg='#2F4F4F')
        self.labelPreço.place(relx=0.54, rely=0.3)
        self.entryPreço = Entry(self.topFrame)
        self.entryPreço.place(relx=0.56, rely=0.44, relwidth=0.09)

        self.labelDistribuidora = Label(self.topFrame, text='Distribuidora', bg='#F0E68C', font='bold', fg='#2F4F4F')
        self.labelDistribuidora.place(relx=0.4, rely=0.55)
        self.entryDistribuidora = Entry(self.topFrame)
        self.entryDistribuidora.place(relx=0.4, rely=0.68, relwidth=0.44)

        self.labelId = Label(self.topFrame, text='Código Produto', bg='#F0E68C', font='bold', fg='#2F4F4F')
        self.labelId.place(relx=0.7, rely=0.3)
        self.entryId = Entry(self.topFrame)
        self.entryId.place(relx=0.72, rely=0.44, relwidth=0.09)

    def criarBotões(self):
        self.btnCadastar = Button(self.topFrame, text='CADASTRAR', bg='#696969', fg='white')
        self.btnCadastar.place(relx=0.89, rely=0.2)

        self.btnCadastar = Button(self.topFrame, text='ATUALIZAR', bg='#696969', fg='white')
        self.btnCadastar.place(relx=0.89, rely=0.4, relwidth=0.1)

        self.btnCadastar = Button(self.topFrame, text='DELETAR', bg='#696969', fg='white')
        self.btnCadastar.place(relx=0.89, rely=0.6, relwidth=0.1)

        self.btnCadastar = Button(self.topFrame, text='LIMPAR', bg='#696969', fg='white')
        self.btnCadastar.place(relx=0.89, rely=0.78, relwidth=0.1)
    def criarTabelaProdutos(self):
        self.tabelaProdutos = ttk.Treeview(self.botomFrame, column=('col1', 'col2', 'col3', 'col4', 'col5'))
        self.tabelaProdutos.heading('#0', text='')
        self.tabelaProdutos.heading('#1', text='Código')
        self.tabelaProdutos.heading('#2', text='Nome')
        self.tabelaProdutos.heading('#3', tex='Preço')
        self.tabelaProdutos.heading('#4', text='Quantidade')
        self.tabelaProdutos.heading('#5', text='Distribuidora')

        self.tabelaProdutos.column('#0', width=0)
        self.tabelaProdutos.column('#1', width=50)
        self.tabelaProdutos.column('#2', width=100)
        self.tabelaProdutos.column('#3', width=100)
        self.tabelaProdutos.column('#4', width=100)
        self.tabelaProdutos.column('#5', width=200)
        self.tabelaProdutos.place(relx=0.01, rely=0.01, relwidth=0.69, relheight=0.98)


Aplicação()
