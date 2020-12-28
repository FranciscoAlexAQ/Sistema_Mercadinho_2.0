from Conexao import Conexao
import sqlite3


# função responsável por cadastrar todos os regitros na tabela
class Cadastrar:
    def cadastrarProdutos(self, nome, preco, quantidade, distribuidora):
        try:
            self.conn = Conexao.conectarBanco(self)
            self.cursor = self.conn.cursor()
            self.cursor.execute(f'INSERT INTO produtos (nome, preco, quantidade, distribuidora) VALUES ("{nome}", {preco}, {quantidade}, "{distribuidora}")')
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print(e)
