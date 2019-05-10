import os, subprocess

matricula = os.environ['USERNAME']
equipamento = os.environ['ComputerName']

print(matricula)

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

matricula = os.environ['USERNAME']
usuario_logado = pega_nome_usuario_logado(matricula) #os.environ['USERNAME']#