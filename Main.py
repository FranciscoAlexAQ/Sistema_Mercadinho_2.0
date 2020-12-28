from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import Cadastrar
import Listar
import Atualizar
import Deletar

janela = Tk()


# Esta class traz métodos de verificação e eventos
class FunçõesExtras:

    # Limpa todos os campos
    def limparCampos(self):
        self.entryNome.delete(0, END)
        self.entryPreço.delete(0, END)
        self.entryQuantidade.delete(0, END)
        self.entryDistribuidora.delete(0, END)
        self.entryId.delete(0, END)

    # Ao fazer duplo clique em um registro, colocar os valores desse registro nos seus respctivos campos
    def duploClique(self, event):
        self.tabelaProdutos.selection()

        for i in self.tabelaProdutos.selection():
            col1, col2, col3, col4, col5 = self.tabelaProdutos.item(i, 'values')
            self.entryId.insert(END, col1)
            self.entryNome.insert(END, col2)
            self.entryPreço.insert(END, col3)
            self.entryQuantidade.insert(END, col4)
            self.entryDistribuidora.insert(END, col5)

    # Verifica se todos os campos estão preenchidos antes de atualizar
    def atualizarVerifica(self):
        if self.entryId.get() == '' or self.entryNome.get() == '' or self.entryPreço.get() == '' or self.entryQuantidade.get() == '' or \
                self.entryDistribuidora.get() == '':
            print(messagebox.showinfo('Campos Vazio', 'Dê um duplo clique em um registro da tabela para atualizá-lo'))
        else:
            Atualizar.Atualizar.atualizarProdutos(self, int(self.entryId.get()), self.entryNome.get(), float(self.entryPreço.get()),
                                                  int(self.entryQuantidade.get()), self.entryDistribuidora.get())

    # Verifica se o campo 'código' está vazio, se tiver, não excluir produto
    def deletarVerifica(self):
        if self.entryId.get() == '':
            print(messagebox.showinfo('Campo Vazio', 'Por favor, informe o código do produto para excluir'))
        else:
            Deletar.Deletar.deletarProdutos(self, int(self.entryId.get()))


# Classe principal
class Aplicação(FunçõesExtras):
    def __init__(self):
        self.configurarDaTela()
        self.criarFrames()
        self.LabelsEntrys()
        self.criarBotões()
        self.criarTabelaProdutos()
        janela.mainloop()

    # configuração da tela principal
    def configurarDaTela(self):
        janela.title('Cadastro de Produtos')
        janela.geometry('800x600')
        janela.resizable(True, True)
        janela.minsize(width=760, height=492)
        janela.maxsize(width=900, height=520)
        janela.configure(bg='#F0E68C')

    # criação e posicionamento dos Frames
    def criarFrames(self):
        self.topFrame = Frame(janela, bg='#F0E68C', bd=4, highlightbackground='#696969', highlightthickness=3)
        self.topFrame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.5)

        self.botomFrame = Frame(janela, bg='#F0E68C', bd=3, highlightbackground='#696969', highlightthickness=3)
        self.botomFrame.place(relx=0.01, rely=0.52, relwidth=0.98, relheight=0.47)

    # criação e posicionamento dos Labels e Entrys
    def LabelsEntrys(self):

        self.icone = PhotoImage(file='img\\icone2.png')
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

    # criação, posicionamento e atribuição de funções aos botões
    def criarBotões(self):
        self.btnCadastar = Button(self.topFrame, text='CADASTRAR', bg='#696969', fg='white', command=lambda:
                    [Cadastrar.Cadastrar.cadastrarProdutos(self, str(self.entryNome.get()).title(),
                    float(self.entryPreço.get()), int(self.entryQuantidade.get()),
                    str(self.entryDistribuidora.get()).title()), self.limparCampos(), self.criarTabelaProdutos()])
        self.btnCadastar.place(relx=0.89, rely=0.2)

        self.btnAtualizar = Button(self.topFrame, text='ATUALIZAR', bg='#696969', fg='white', command=lambda:
            [self.atualizarVerifica(), self.limparCampos(), self.criarTabelaProdutos()])
        self.btnAtualizar.place(relx=0.89, rely=0.4, relwidth=0.1)

        self.btnDeletar = Button(self.topFrame, text='DELETAR', bg='#696969', fg='white', command=lambda:
            [self.deletarVerifica(), self.limparCampos(), self.criarTabelaProdutos()])
        self.btnDeletar.place(relx=0.89, rely=0.6, relwidth=0.1)

        self.btnLimpar = Button(self.topFrame, text='LIMPAR', bg='#696969', fg='white', command=self.limparCampos)
        self.btnLimpar.place(relx=0.89, rely=0.78, relwidth=0.1)

    # criação, posicionamento e preenchimento da tabela
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

        # comando pertecente à função duploClique
        self.tabelaProdutos.bind('<Double-1>', self.duploClique)
        self.tabelaProdutos.place(relx=0.01, rely=0.01, relwidth=0.69, relheight=0.98)

        # Insere os registros na tabela
        self.tabelaProdutos.delete(*self.tabelaProdutos.get_children())
        for i in Listar.Listar.listarProdutos(self):
            self.tabelaProdutos.insert('', END, values=i)


Aplicação()
