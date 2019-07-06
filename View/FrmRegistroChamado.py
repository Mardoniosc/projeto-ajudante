
# Pacotes nativos do Python
import sys, os

# Pacotes de terceiros
from PyQt5.QtWidgets import QApplication,QWidget, QErrorMessage, QMessageBox
from PyQt5.uic import loadUi

# Meus Pacotes
from Controller.RegistroChamadoCTR import RegistroChamadoCTR
from Diversos.recursos import pega_nome_usuario_logado,criar_mostrar_data, teste_conexao, Mbox, criar_hora_guardar


# VARIAVEIS GLOBAIS
DATA_HOJE = criar_mostrar_data(1)
HORA = criar_hora_guardar()
MATRICULA = os.environ['USERNAME']
USUARIO_LOGADO = pega_nome_usuario_logado(MATRICULA)


class FrmRegistroChamado(QWidget):
    def __init__(self):
        super(FrmRegistroChamado, self).__init__()
        loadUi('view/UI/FrmRegistroDeChamados.ui', self)
        self.setWindowTitle('Registro de Chamados')

        self.input_data.setText(DATA_HOJE)
        self.input_atendente.setText(USUARIO_LOGADO)
        self.check_critico.stateChanged.connect(self.doCheck_critico)
        self.check_vip.stateChanged.connect(self.doCheck_vip)

        # BOTÕES DE CLICK
        self.buttonRegistrarChamado.clicked.connect(self.click_registrar)

    def click_registrar(self):
        conexao = teste_conexao()
        if conexao == True:
            resultado_insert = self.grava_campos()
            print(resultado_insert)
            if resultado_insert == True:
                self.limpar_dados()
                QMessageBox.information(self, "Chamado", "Chamado registrado com sucesso!")
            else:
                resultado_insert = str(resultado_insert)
                if resultado_insert.__contains__('Duplicate'):
                    QMessageBox.critical(self, 'Erro ao registrar o chamados', "Chamado já registrado no Banco de dados!")
                else:
                    QMessageBox.critical(self, 'Erro ao registrar o chamados',
                                         "Favor encaminhar erro para Mardonio caso persista \nERROR:\n\n %s" % resultado_insert)

        else:
            texto_erro = str(conexao)
            QErrorMessage.showMessage(self, "Erro de conexão")
            Mbox("Erro conexão", texto_erro, 0)

    def limpar_dados(self):
        self.input_chamado.setText("")
        self.input_problema.setText("")
        self.input_nomeLogico.setText("")
        self.input_atendente.setText(USUARIO_LOGADO)
        self.box_status.setCurrentText("CONCLUÍDO")
        self.check_vip.setChecked(False)
        self.check_critico.setChecked(False)


    def grava_campos(self, opcao=1):
        # Atendente verifica se tem algo escrito
        if self.input_atendente.text() == "":
            atendente = self.input_atendente.placeholderText()
        else:
            atendente = self.input_atendente.text()

        # Numero do chamado
        if self.input_chamado.text() == "":
            chamado = self.input_chamado.placeholderText()
        else:
            chamado = self.input_chamado.text()

        # problema do chamados
        if self.input_problema.text() == "":
            problema = self.input_problema.placeholderText()
        else:
            problema = self.input_problema.text()

        # Nome logico
        if self.input_nomeLogico.text() == "":
            nome_logico = self.input_nomeLogico.placeholderText()
        else:
            nome_logico = self.input_nomeLogico.text()

        # status
        status = self.box_status.currentText()

        # função para inserir os dados no banco de dados Mysql
        data_guardar = int(criar_mostrar_data(0))
        hora_guardar = criar_hora_guardar()
        vip = self.doCheck_vip()
        critico = self.doCheck_critico()

        if opcao == 1:
            inserir_resultado = RegistroChamadoCTR.inserrir(data_guardar, atendente, chamado, problema, status, nome_logico,
                                                 vip,critico, hora_guardar)
            return inserir_resultado
        # elif opcao == 2:
        #     id_chamado = int(self.input_id.text())
        #     atualiza_resultado = atualiza_registro(id_chamado, data_guardar, atendente, chamado, problema,
        #                                            status, nome_logico, vip, critico, hora_guardar)
        #     return atualiza_resultado
        # else:
        #     pass

    def doCheck_critico(self):
        if self.check_critico.isChecked():
            critico = 1
        else:
            critico = 0
        return critico

    def doCheck_vip(self):
        if self.check_vip.isChecked():
            vip = 1
        else:
            vip = 0
        return vip


if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmRegistroChamado()
    widget.show()
    sys.exit(app.exec())

