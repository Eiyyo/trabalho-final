# impottando bibliotecas
from time import sleep
import tkinter as tk

# criação da janela selecionar opção
janela_selecionar = tk.Tk()
janela_selecionar.geometry("900x506")
janela_selecionar.title("selecionar")


# imagem de fundo
imagem = tk.PhotoImage(
    file=r"C:\Users\Guilherme Freire\Desktop\projeto\P.O.G.E.R.S\selecionar.png"
)

# label da imagem de fundo
label_fundo = tk.Label(janela_selecionar, image=imagem)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# botao excluir

# impottando bibliotecas

import mysql.connector

# inicio da conexao com o servidor
conexao = mysql.connector.connect(
    host="localhost", user="root", password="0106", database="cadastroprodutos"
)

# criação docursor para executar os comandos sql
cursor = conexao.cursor()


# criação da janela excluir produtos
def excluir_produtos():
    janela_selecionar.destroy()
    sleep(1)
    janela_excluirprodutos = tk.Tk()
    janela_excluirprodutos.geometry("900x506")
    janela_excluirprodutos.title("excluir_produtos")

    def excluir():
        # inicio da conexao com o servidor
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="0106", database="cadastroprodutos"
        )

        # criação docursor para executar os comandos sql
        cursor = conexao.cursor()

        codigoproduto = codigoproduto1.get()
        comando = (
            f'DELETE FROM cadastroprodutos WHERE codigoproduto = "{codigoproduto}"'
        )
        cursor.execute(comando)
        conexao.commit()  # edita o banco dedados

        # encerrando conexao e cursor(fazer isso no final de todas as defs do crud)
        cursor.close()
        conexao.close()

    # imagem de fundo
    imagem = tk.PhotoImage(
        file=r"C:\Users\Guilherme Freire\Desktop\projeto\P.O.G.E.R.S\excluirproduto.png"
    )

    # label da imagem de fundo
    label_fundo = tk.Label(janela_excluirprodutos, image=imagem)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    # botao excluir
    botao2 = tk.Button(
        janela_excluirprodutos, text="excluir", command=excluir, borderwidth=0
    )
    botao2.place(x=750, y=60)

    # campo de texto codigo do produto
    codigoproduto1 = tk.Entry(janela_excluirprodutos)
    codigoproduto1.place(x=208, y=219)

    # comando para manter a janela principal aberta
    janela_excluirprodutos.mainloop()


#
botao2 = tk.Button(
    janela_selecionar, text="excluir", command=excluir_produtos, borderwidth=0
)
botao2.place(x=750, y=60)

# botao adicionar

# impottando bibliotecas
import mysql.connector

# inicio da conexao com o servidor
conexao = mysql.connector.connect(
    host="localhost", user="root", password="0106", database="cadastroprodutos"
)

# criação docursor para executar os comandos sql
cursor = conexao.cursor()


# criação da janela adicionar produtos
def adicionar_produtos():
    janela_selecionar.destroy()
    sleep(1)
    janela_adicionarprodutos = tk.Tk()
    janela_adicionarprodutos.geometry("900x506")
    janela_adicionarprodutos.title("adicionar_produtos")

    # def para adicionar produtos
    def criar():
        # inicio da conexao com o servidor
        conexao = mysql.connector.connect(
            host="localhost", user="root", password="0106", database="cadastroprodutos"
        )

        # criação docursor para executar os comandos sql
        cursor = conexao.cursor()

        codigoproduto = codigoproduto1.get()
        produto = produto1.get()
        precocompra = float(precocomra1.get())
        precovenda = float(precovenda1.get())
        quantidade = int(quantidade1.get())
        comando = f' INSERT INTO cadastroprodutos (codigoproduto, produto, precocompra, precovenda, quantidade) VALUES ("{codigoproduto}","{produto}",{precocompra},{precovenda},{quantidade})'
        cursor.execute(comando)
        conexao.commit()  # edita o banco dedados

        # encerrando conexao e cursor(fazer isso no final de todas as defs do crud)
        cursor.close()
        conexao.close()

    # imagem de fundo
    imagem = tk.PhotoImage(
        file=r"C:\Users\Guilherme Freire\Desktop\projeto\P.O.G.E.R.S\adicionarprodutos.png"
    )

    # label da imagem de fundo
    label_fundo = tk.Label(janela_adicionarprodutos, image=imagem)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    # botao adicionar
    botao = tk.Button(
        janela_adicionarprodutos, text="adicionar", command=criar, borderwidth=0
    )
    botao.place(x=611, y=60)

    # campo de  texto produto
    produto1 = tk.Entry(janela_adicionarprodutos)
    produto1.place(x=141, y=174)

    # campo de  texto precocompra
    precocomra1 = tk.Entry(janela_adicionarprodutos)
    precocomra1.place(x=197, y=264)

    # campo de  texto precovenda
    precovenda1 = tk.Entry(janela_adicionarprodutos)
    precovenda1.place(x=186, y=312)

    # campo de  texto quantidade
    quantidade1 = tk.Entry(janela_adicionarprodutos)
    quantidade1.place(x=141, y=355)

    # campo de texto codigo do produto
    codigoproduto1 = tk.Entry(janela_adicionarprodutos)
    codigoproduto1.place(x=208, y=219)

    # comando para manter a janela principal aberta
    janela_adicionarprodutos.mainloop()


#

botao = tk.Button(
    janela_selecionar, text="adicionar", command=adicionar_produtos, borderwidth=0
)
botao.place(x=611, y=60)

# comando para manter a janela principal aberta
janela_selecionar.mainloop()
