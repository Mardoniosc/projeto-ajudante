# coding: utf-8
import mysql.connector

class ConexaoBDMySql(object):
    DADOS_CONEXAO = None

    def __init__(self, database, usr, pwd, mhost):
        self.DADOS_CONEXAO = mysql.connector.connect(db=database, user=usr, passwd=pwd, host=mhost)

    def manipular(self, sql):
        try:
            cur = self.DADOS_CONEXAO.cursor()
            cur.execute(sql)
            cur.close()
            self.DADOS_CONEXAO.commit()
        except:
            return False

    def consulta(self, sql):
        rs = None
        try:
            cur = self.DADOS_CONEXAO.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
        except:
            return None
        return rs

    def fechar(self):
        self.DADOS_CONEXAO.close()