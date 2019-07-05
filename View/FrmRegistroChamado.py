
# Pacotes nativos do Python
import sys, os

# Pacotes de terceiros
from PyQt5.QtWidgets import QApplication,QWidget, QErrorMessage
from PyQt5.uic import loadUi

# Meus Pacotes
from Controller.RegistroChamadoCTR import RegistroChamadoCTR
from Diversos.recursos import pega_nome_usuario_logado,criar_mostrar_data, teste_conexao, Mbox


# VARIAVEIS GLOBAIS
DATA_HOJE = criar_mostrar_data(1)
MATRICULA = os.environ['USERNAME']
USUARIO_LOGADO = pega_nome_usuario_logado(MATRICULA)

class FrmRegistroChamado(QWidget):
    def __init__(self):
        super(FrmRegistroChamado, self).__init__()
        loadUi('view/UI/FrmRegistroDeChamados.ui', self)
        self.setWindowTitle('Registro de Chamados')

        self.input_data.setText(DATA_HOJE)
        self.input_atendente.setText(USUARIO_LOGADO)

        # BOTÕES DE CLICK
        self.buttonRegistrarChamado.clicked.connect(self.click_registrar)

    def click_registrar(self):
        print("informações necessárias sendo coletadas aqui")
        conexao = teste_conexao()
        if conexao == True:
            print('continue')
            # try:
            #     resulta = RegistroChamadoCTR.inserrir(DATA_HOJE,USUARIO_LOGADO,)
        else:
            texto_erro = str(conexao)
            QErrorMessage.showMessage(self, "Erro de conexão")
            Mbox("Erro conexão", texto_erro, 0)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmRegistroChamado()
    widget.show()
    sys.exit(app.exec())

