#coding: utf-8
import sys, mysql.connector
from Diversos.ConexaoBancoDeDadosMySQL import ConexaoBDMySql
# con = ConexaoBDMySql("RegistroDB", "admin", "rktd*77Imo", "192.168.0.100")
con = ConexaoBDMySql("sd_chamados", "sd", "sd", "DF7562NT713")


class RegistroAutomaticoDAO:
    @staticmethod
    def registrar_chamado(dados):
        try:
            sql = "insert into registros  (id,data_registro,atendente,chamado,problema,estatus,nome_logico,vip,critico," \
                  "hora_registro)" \
                  "VALUES (null,%d,'%s','%s','%s','%s','%s',%d,%d,'%s')" % (
                dados.Data_registro, dados.Atendente, dados.Chamado, dados.Problema, dados.Status, dados.Nome_logico,
                dados.Vip, dados.Critico, dados.Hora_registro)
            resultado = con.manipular(sql)
            return resultado
        except Exception as e:
            print(e)
            # print("Erro na execução de script dentro do banco de dados")
            return e, False