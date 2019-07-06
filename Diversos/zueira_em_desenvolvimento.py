# coding: utf-8
import win32com.client, os
from Diversos.recursos import pega_nome_usuario_logado

MATRICULA = os.environ['USERNAME']
USUARIO_LOGADO = pega_nome_usuario_logado(MATRICULA) #os.environ['USERNAME']#


def mandar_email():
    emails = "<p772920@mail.caixa>"
    const = win32com.client.constants
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = "Botão que ta em desenvolvimento!!"
    newMail.Body = "O %s parece que é doente, clicou mais de 10x no botão que você disse que ta em desenvolvimento!" % USUARIO_LOGADO

    newMail.To = emails
    newMail.display()
    newMail.Send() # Aqui enviar o email de forma automatica


def zueira(numero_de_Click):

    if numero_de_Click == 1:
        return ("Em Desenvolvimento", "Em desenvolvimento favor aguarde!")

    elif numero_de_Click == 2:
        return ("Em Desenvolvimento", "Uma imagem vale mais do que mil palavras, "
                                      "mas ocupa 3 mil vezes mais espaço em disco.\n\n"
                                      ""
                                      "Eu Disse aguarde em desenvolvimento!")

    elif numero_de_Click == 3:
        return ("Em Desenvolvimento", "Eu disse que ta em DESENVOLVIMENTO, "
                                      ""
                                      "\n\n #### FAVOR AGUARDE #### !!!")

    elif numero_de_Click == 4:
        return ("Em Desenvolvimento", "Pergunta, você não tem chamado para atender não?\n\n"
                                      "para de clicar é melhor para você")

    elif numero_de_Click == 5:
        return ("Em Desenvolvimento", "Cuida de sua vida cara, fica perdendo tempo clicando em algo que não funciona\n\n"
                                      ""
                                      "só lembrando esta desenvolvimento")
    elif numero_de_Click == 6:
        return ("Em Desenvolvimento", "Falando sério acho que tu é DOENTE, né possivel o cara continuar "
                                      "clicando na p#$%@ do botão que diz que ta em DESENVOLVIMENTO")



    elif numero_de_Click > 6 and numero_de_Click < 9:
        return ('Em Desenvolvimento', 'Para de clicar essa já é a %dº vez que você clica' % numero_de_Click)

    elif numero_de_Click == 9:
        return ('Em desenvimento', 'Clica de novo para você ver')

    elif numero_de_Click == 10:
        return ("Em Desenvolvimento", "Mardonio vai ficar sabendo que você tem probleminha na cabeça, "
                                      "se clicar de novo vou mandar um e-mail para ele.")
    elif numero_de_Click == 11:
        mandar_email()
        return ("Em Desenvolvimento", "Falei para você para de clicar mano")

    elif numero_de_Click == 12:
        return "Em Desenvolvimento", 'Parei pode continuar clicando ai feito abestado até o 50'

    elif numero_de_Click == 30:
        return ("Em Desenvolvimento", "Nossa ta chato isso, ter que ir no menu toda hora, cansei já! :O")
    elif numero_de_Click < 50:
        return ("Em Desenvolvimento", "Tu é chato mesmo! se vai cansar \n\n"
                                      "não sabe quantos faltam ainda")

    else:
        return ("Em Desenvolvimento", "Meu deus para de clicar nessa parada")

    # elif numero_de_Click == 4:
    #
    #     return ("Em Desenvolvimento", "")
