# coding: utf-8
import sys, subprocess
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.uic import loadUi
from Controller.EncaminhamentoCTR import EncaminhamentoCTR
NOTAS = "\\\\DF7562NT713\Mardonio$\\Notas"
# NOTAS = "C:\dev\\Notas_Gerador\\Notas"

class FrmEncaminhamento(QWidget):
    def __init__(self):
        super(FrmEncaminhamento, self).__init__()
        loadUi('view/UI/FrmEncaminhamento.ui', self)
        self.setWindowTitle('Encaminhamento')

        self.thread = QThread()
        self.notapadra = AbrirNotaPadrao()

        self.notapadra.moveToThread(self.thread)
        self.thread.started.connect(self.notapadra.abrirNotaPadrao)

        self.notapadra.finished.connect(self.fim_do_processo_paralelo)

        # Botões aba Encaminhamento
        self.button_gerar_nota_encaminhamento.clicked.connect(self.gerar_nota_encaminhamento)

        # função aba encaminhamento
    def gerar_nota_encaminhamento(self):
        problema = self.input_problema.text()
        diagnostico = self.input_diagnostico.text()
        procedimento_realizado = self.input_procedimento_realizado.text()
        msg_erro = self.input_mensage_erro.text()
        momento_msg_erro = self.input_situacao_mensagem.text()
        motivo_enc = self.input_motivo_encaminhamento.text()
        if self.radio_sim_2.isChecked():
            imagem_anexo = "Sim"
        else:
            imagem_anexo = "Não"

        fila = self.box_fila_encaminhamento.currentText()
        tipo_nota = self.box_tipo_nota_encaminhamento.currentText()

        # print(problema,diagnostico,procedimento_realizado,msg_erro,momento_msg_erro,motivo_enc,imagem_anexo,
        #       fila,tipo_nota)

        EncaminhamentoCTR.nota_encaminhamento(problema, diagnostico, procedimento_realizado, msg_erro,
                                              momento_msg_erro,
                                              motivo_enc, imagem_anexo, fila, tipo_nota)
        # FechamentoCTR.nota_fechamento(usuario, ocorrencia, procedimento, fila, acompanhamento, orientacao, tipo_nota)

        self.input_problema.setText("")
        self.input_diagnostico.setText("")
        self.input_procedimento_realizado.setText("")
        self.input_mensage_erro.setText("")
        self.input_situacao_mensagem.setText("")
        self.input_motivo_encaminhamento.setText("")
        self.thread.start()

    def fim_do_processo_paralelo(self):
        self.thread.quit()


class AbrirNotaPadrao(QObject):
    finished = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def abrirNotaPadrao(self):
        osCommandString = ("notepad %s/NotaPadrao.txt" % NOTAS)
        try:
            subprocess.Popen(osCommandString, shell=True)
        except:
            print("Erro não foi possivel abrir o NOTAPADRAO")
        self.finished.emit()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmEncaminhamento()
    widget.show()
    sys.exit(app.exec())