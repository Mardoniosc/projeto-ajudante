# coding: utf-8
import mysql.connector, ctypes

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

class ConexaoBDMySql(object):
    DADOS_CONEXAO = None

    def __init__(self, database, usr, pwd, mhost):
        from Diversos.recursos import Mbox
        try:
            self.DADOS_CONEXAO = mysql.connector.connect(db=database, user=usr, passwd=pwd, host=mhost)
        except Exception as e:
            print(e)
            mensagem_de_erro = str(e)
            Mbox("Erro de conexão", mensagem_de_erro, 0)

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