from backend.Conexao import Conexao
import sqlite3


class Deletar:
    def deletarProdutos(self, id):
        try:
            self.conn = Conexao.conectarBanco(self)
            self.cursor = self.conn.cursor()
            self.cursor.execute(f'DELETE FROM produtos WHERE id = {id}')
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print(e)
