import sqlite3
import os


class Conexao:
    def conectarBanco(self):
        try:
            self.conect = sqlite3.connect(os.path.dirname(__file__) + '\cadastroDeProdutos.db')
        except sqlite3.Error as e:
            print(e)
        return self.conect

    def criarTabela(self):
        try:
            self.conn = self.conectarBanco()
            self.cursor = self.conn.cursor()
            self.cursor.execute('CREATE TABLE produtos (id INTEGER PRIMARY KEY, nome VARCHAR(30), '
                                'preco INTEGER, quantidade INTEGER, distribuidora VARCHAR(30))')
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print(e)
