import xlrd, ctypes, subprocess
from datetime import datetime, date

def leitorDeArquivoXLS():
    arquivo = 'C:\Rel_Diario\\relatorio.xls'
    tabela = xlrd.open_workbook(arquivo).sheet_by_index(0)
    qtd_linhas = tabela.nrows
    linhas = []
    for i in range(1, qtd_linhas):
        if tabela.row(i)[0].value == '':
            break
        linhas.append(
            {
                # COLUNAS PEGAS 1,3,15,22,58,59,
                'linha': i + 1,
                'ordemDeTrabalho': tabela.row(i)[0].value,
                'status': tabela.row(i)[2].value,
                'data_hora_conclusao': tabela.row(i)[14].value,
                'nome_logico': tabela.row(i)[21].value,
                'software': tabela.row(i)[57].value,
                'procedimento_solicitado': tabela.row(i)[58].value,

            }
        )
    return linhas

def criar_hora_guardar():
    now = datetime.now()
    hora_agora = str(now.hour)
    minuto_agora = str(now.minute)
    segundo_agora = str(now.second)
    if len(hora_agora) == 1:
        hora_agora = "0"+hora_agora
    if len(minuto_agora) == 1:
        minuto_agora = "0"+minuto_agora
    if len(segundo_agora) == 1:
        segundo_agora = "0"+segundo_agora
    hora_atual = str(hora_agora+":"+minuto_agora+":"+segundo_agora)

    return hora_atual

def criar_mostrar_data(data):
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    data_mostrar = "%.2d/%.2d/%d" % (dia,mes,ano)
    data_guardar = "%d%.2d%.2d" % (ano,mes,dia)
    if data == 1:
        return data_mostrar
    else:
        return data_guardar

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    ##  Styles:
    ##  0 : OK
    ##  1 : OK | Cancel
    ##  2 : Abort | Retry | Ignore
    ##  3 : Yes | No | Cancel
    ##  4 : Yes | No
    ##  5 : Retry | No
    ##  6 : Cancel | Try Again | Continue

def func_devolve_nome_logico(nomeLogico):
    nome_logico = nomeLogico.split('\n\n')
    for x in nome_logico:
        if x.__contains__('Nome Lógico') or x.__contains__('Nome lógico'):
            nome_logico = x
            break
        else:
            nome_logico = 'Nome Lógico: DF0000ET001'
    nome_logico = nome_logico[-12:]
    nome_logico = nome_logico.strip()
    return nome_logico

def guardar_data(data):
    dia = int(data[:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    data_guardar = int("%d%.2d%.2d" % (ano,mes,dia))

    return data_guardar


def pega_nome_usuario_logado(matricula):

    comando_verifica_nome = ("net user /domain %s | FIND /I \"Nome Completo\"" % (matricula))
    try:
        nome_atendente =str(subprocess.check_output(comando_verifica_nome, shell=True))
    except:
        return False
    nome =str(nome_atendente[38:])
    nome_sobrenome = (nome.split('\\r\\n'))
    nome_sobrenome = (nome_sobrenome[0].split(' - CETEC'))
    nome_a_mostrar_guardar = (nome_sobrenome[0])
    return nome_a_mostrar_guardar