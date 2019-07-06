from os import path, environ
import sys

from Controller.RegistroAutomaticoCTR import RegistroAutomaticoCTR
from Diversos.Funcoes_auxiliares import *

MATRICULA = environ['USERNAME']
USUARIO_LOGADO = pega_nome_usuario_logado(MATRICULA) #os.environ['USERNAME']#

class RegistroAutomaticoDeChamados:
    def __init__(self):
        relatorio = 'C:\Rel_Diario\\Relatorio.xls'
        if not path.exists(relatorio):
            Mbox("Erro relatorio não encontrado", "Não foi encontrado o arquivo 'Relatorio.xls'\n"
                                 "Favor gerar o arquivo e salvar no seguinte caminho:\n"
                                 " C:\Rel_Diario\Relatorio.xls\n"
                                 "após salvar execute o programa novamente", 0)
            sys.exit()
        self.registrar_chamado()



    def registrar_chamado(self):
        resultado = leitorDeArquivoXLS()
        chamadosCadastrados = 0
        chamadoJaCadastrados = 0


        for x in resultado:
            chamado = x['ordemDeTrabalho']
            status = x['status']
            data = guardar_data(x['data_hora_conclusao'][:10])
            hora = x['data_hora_conclusao'][-8:]
            nome_logico = func_devolve_nome_logico(x['nome_logico'])
            problema = x['software']
            resultado  = RegistroAutomaticoCTR.registrarChamado(data, USUARIO_LOGADO, chamado, problema, status,
                                                                nome_logico, 0, 0, hora)
            if resultado == True:
                chamadosCadastrados = chamadosCadastrados + 1
            elif resultado == False:
                chamadoJaCadastrados = chamadoJaCadastrados + 1

            else:
                print(resultado)
        Mbox("Processo Finalizado",("Chamados cadasstrado agora: %d"
              "\nChamados que já estavam cadastrados: %d" % (chamadosCadastrados, chamadoJaCadastrados)),0)