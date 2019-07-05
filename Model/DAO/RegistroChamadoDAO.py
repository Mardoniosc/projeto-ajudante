# coding: utf-8
from Diversos.ConexaoBancoDeDadosMySQL import ConexaoBDMySql
con = ConexaoBDMySql("sd_chamados", "sd", "sd", "DF7562NT713")

class RegistroChamadoDAO:

    # Exemplo de recebimento dos dados
    @staticmethod
    def print_dados(dados):
        print(dados.Atendente)
        print(dados.Vip)
        print(dados.NomeLogico)
        print(dados.Status)

    @staticmethod
    def pesquisar(tipo, dados):
        print(dados.Atendente)
        print(dados.Chamado)

        if tipo == 1:
            sql = "select * from registros WHERE atendente='%s'" % dados.Atendente
            resultado = con.consulta(sql)
            con.fechar()
            return resultado

        elif tipo == 4:
            sql = "select * from registros WHERE chamado = '%s';" % dados.Chamado
            resultado = con.consulta(sql)
            con.fechar()
            return resultado

    def excluir(self, dados):
        sql = ("DELETE FROM `registros` WHERE `registros`.`chamado` = '%s';" % dados.Chamado)
        resultado = con.manipular(sql)
        con.fechar()
        return resultado

    def inserir(self, dados):

        sql = "insert into registros  (id,data_registro,atendente,chamado,problema,estatus,nome_logico,vip,critico,hora_registro)" \
              "VALUES (null,%d,'%s','%s','%s','%s','%s',%d,%d,'%s')" % (
              dados.DataRegistro, dados.Atendente, dados.Chamado, dados.Problema, dados.Status,
              dados.NomeLogico, dados.Vip, dados.Critico, dados.HoraRegistro)
        resultado = con.manipular(sql)
        con.fechar()
        return resultado

    def atualizar(self, dados):
        sql = ("UPDATE `registros` SET `data_registro` = %d, `atendente` = '%s', `chamado` = '%s', `problema` = '%s', "
               "`estatus` = '%s', `nome_logico` = '%s', `vip` = %d, `critico` = %d, "
               "`hora_registro` = '%s' WHERE `registros`.`id` = %d;" % (
            dados.DataRegistro, dados.Atendente, dados.Chamado, dados.Problema, dados.Status,
            dados.NomeLogico, dados.Vip, dados.Critico, dados.HoraRegistro, dados.Id))
        resultado = con.manipular(sql)
        con.fechar()
        return resultado
