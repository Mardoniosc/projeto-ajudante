# coding: utf-8

import time, subprocess, os

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