from backend.Conexao import Conexao
import sqlite3


class Listar:
    def listarProdutos(self):
        try:
            self.conn = Conexao.conectarBanco(self)
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT * FROM produtos ORDER BY id')
            self.dados = self.cursor.fetchall()
            self.conn.close()
            return self.dados
        except sqlite3.Error as e:
            print(e)

