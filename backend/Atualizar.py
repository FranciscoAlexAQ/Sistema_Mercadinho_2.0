from backend.Conexao import Conexao
import sqlite3


class Atualizar:
    def atualizarProdutos(self, id, nome, preco, quantidade, distribuidora):
        self.conn = Conexao.conectarBanco(self)
        self.cursor = self.conn.cursor()
        self.cursor.execute(F'UPDATE produtos SET nome = "{nome}", preco = {preco}, '
                            F'quantidade = {quantidade}, distribuidora = "{distribuidora}" WHERE id = {id}')
        self.conn.commit()
        self.conn.close()
