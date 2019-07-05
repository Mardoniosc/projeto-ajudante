# coding: utf-8

import time, subprocess, ctypes
from datetime import datetime, date

from Diversos.ConexaoBancoDeDadosMySQL import ConexaoBDMySql


def conexao_remota(nome_logico, usuario, senha):
    cmdkey = 'cmdkey /generic:TERMSRV/%s /user:%s /pass:%s' % (nome_logico, usuario, senha)
    subprocess.call(cmdkey, shell=True)

    mstsc = 'mstsc /f /v:%s' % nome_logico
    subprocess.call(mstsc, shell=True)
    time.sleep(5)

    cmdkey = 'cmdkey /delete:TERMSRV/%s' % nome_logico
    subprocess.call(cmdkey, shell=True)


def conectarnaEC(nomelogico):

    putty = ("start putty -ssh caixa@%s.diretorio.caixa -pw estacaolivredebian" % nomelogico)
    try:
        subprocess.call(putty, shell=True)

    except subprocess.CalledProcessError as e:
        print ("error code: {}".format(e.returncode))


def conectarnaEF(nomelogico,senha, usuario):
    matricula = usuario
    putty = ("start putty -ssh %s@%s.diretorio.caixa -pw %s" % (matricula, nomelogico, senha))
    try:
        subprocess.call(putty, shell=True)

    except subprocess.CalledProcessError as e:
        print("error code: {}".format(e.returncode))


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

def teste_conexao():
    try:
        ConexaoBDMySql("sd_chamados", "sd", "sd", "DF7562NT713")
        return True
    except Exception as e:
        print(e)
        return e

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