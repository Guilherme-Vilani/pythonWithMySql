import mysql.connector
from tkinter import ttk
import tkinter as tk

resposta = ""

def conexao_banco():
    try:
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='mercado'
        )

        print("deu certo a conexao")
        return cnx
    except:
        print("Deu erro na conexao")


def buscar_todos(tabela):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "SELECT id, descricao, preco FROM {}".format(tabela)
        cursor.execute(query)
        registros = cursor.fetchall()

        return registros

    except:
        print("Não foi possivel selecionar todos da tabela {}".format(tabela))
    
    finally:
        cursor.close()

def buscar_produto_nome(nome, tree):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()
        query = "SELECT * FROM produtos WHERE descricao LIKE '%{}%'".format(nome)
        cursor.execute(query)
        registros = cursor.fetchall()

        for registro in registros:
            tree.insert("", tk.END, values=registro)
        
        return resposta
    
    except:
        print("Não encontrei esse registro")
    
    finally:
        cursor.close()

def cadastra_produto(descricao, cod_barras, preco, id_categoria):
    try:
        conexao = conexao_banco()
        cursor = conexao.cursor()

        query = "INSERT INTO produtos (descricao, cod_barras, preco, id_categoria) values (%s, %s, %s, %s)"

        cursor.execute(query, (descricao, cod_barras, preco, id_categoria))

        conexao.commit()
    except:
        print("Não consegui inserir o registro")