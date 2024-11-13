import tkinter as tk
import database as db
from tkinter import ttk

def abrir_janela_lista_produtos():
    nova_janela = tk.Toplevel()
    nova_janela.title("Listagem de Produtos")
    nova_janela.geometry("600x600")

    # Titulo da minha Janela
    label_titulo = tk.Label(nova_janela, text="Listagem de Produtos")
    label_titulo.pack(pady=10)

    colunas = ("ID", "Descrição", "Preço")
    tabela_produtos = ttk.Treeview(nova_janela, columns=colunas, show="headings")
    tabela_produtos.pack(fill="both")

    # Configura o cabeçalho do coluna
    tabela_produtos.heading("ID", text="ID")
    tabela_produtos.heading("Descrição", text="Descrição")
    tabela_produtos.heading("Preço", text="Preço")

    # Especificar tamanho das colunas
    tabela_produtos.column("ID", width=50)
    tabela_produtos.column("Descrição", width=250)
    tabela_produtos.column("Preço", width=100)

    btn_lista_produtos = tk.Button(nova_janela, text="Listar Produtos", command=lambda:carregar_produtos())
    btn_lista_produtos.pack(pady=10)


    def carregar_produtos():
        registros = db.buscar_todos("produtos")

        for item in tabela_produtos.get_children():
            tabela_produtos.delete(item)

        for registro in registros:
            tabela_produtos.insert("", tk.END, values=registro)

def abrir_janela_cadastro_produto():
    nova_janela = tk.Toplevel()
    nova_janela.title("Cadastro de Produto")
    nova_janela.geometry("400x600")

    # Label e Input da descrição
    label_descricao = tk.Label(nova_janela, text="Descrição")
    label_descricao.pack(pady=0)

    input_descricao = tk.Entry(nova_janela)
    input_descricao.pack(pady=5)

    # Label e Input do preco
    label_preco = tk.Label(nova_janela, text="Preço")
    label_preco.pack(pady=0)

    input_preco = tk.Entry(nova_janela)
    input_preco.pack(pady=5)

    # Label e Input do Cod Barras
    label_cod_barras = tk.Label(nova_janela, text="Cód. Barras")
    label_cod_barras.pack(pady=0)

    input_cod_barras = tk.Entry(nova_janela)
    input_cod_barras.pack(pady=5)

    # Label e Input Id Categoria
    label_id_categoria = tk.Label(nova_janela, text="Categoria")
    label_id_categoria.pack(pady=0)

    input_id_categoria = tk.Entry(nova_janela)
    input_id_categoria.pack(pady=5)

    # Botao que vai cadastrar o produto no banco de dados
    btn_cadastra_produto = tk.Button(nova_janela, text="Cadastrar", command=lambda:db.cadastra_produto(
        input_descricao.get(), 
        input_cod_barras.get(), 
        input_preco.get(), 
        input_id_categoria.get()
        ))
    
    btn_cadastra_produto.pack(pady=10)

def tela_principal():
    root = tk.Tk()
    root.title("Mercado Compre Bem")
    root.geometry("600x600")
    
    btn_abrir_janela_listagem_produtos = tk.Button(root, text="Abrir lista de produtos", command=abrir_janela_lista_produtos)
    btn_abrir_janela_listagem_produtos.pack(pady=10)

    btn_abrir_janela_cadastro_produto = tk.Button(root, text="Cadastrar Produto", command=abrir_janela_cadastro_produto)
    btn_abrir_janela_cadastro_produto.pack(pady=10)
 
    root.mainloop()