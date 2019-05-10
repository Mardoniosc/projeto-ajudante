# coding: utf-8
import sys, os, subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.uic import loadUi
from Controller.FechamentoCTR import FechamentoCTR

NOTAS = "\\\\DF7562NT713\Mardonio$\\Notas"
# NOTAS = "C:\dev\\Notas_Gerador\\Notas"


class FrmFechamento(QWidget):
    def __init__(self):
        super(FrmFechamento, self).__init__()
        loadUi('view/UI/FrmFechamento.ui', self)
        self.setWindowTitle('Fechamento')

        self.thread = QThread()
        self.notapadra = AbrirNotaPadrao()

        self.notapadra.moveToThread(self.thread)
        self.thread.started.connect(self.notapadra.abrirNotaPadrao)

        self.notapadra.finished.connect(self.fim_do_processo_paralelo)

        # Botões aba fechamento
        self.button_gerar_nota.clicked.connect(self.gerar_nota)
        self.box_procedimento.activated.connect(lambda: self.orientacao())
        self.box_tipo_nota.activated.connect(lambda: self.configuracao())

    def gerar_nota(self):
        usuario = self.input_usuario.text()
        ocorrencia = self.input_ocorrencia.text()
        orientacao = self.plainText_orientacao.toPlainText()
        procedimento = self.box_procedimento.currentText()
        fila = self.box_fila.currentText()
        tipo_nota = self.box_tipo_nota.currentText()
        if self.radio_sim.isChecked():
            acompanhamento = "Sim"
        else:
            acompanhamento = "Não"


        FechamentoCTR.nota_fechamento(usuario,ocorrencia,procedimento,fila,acompanhamento,orientacao, tipo_nota)

        self.input_usuario.setText("")
        self.input_ocorrencia.setText("")
        self.plainText_orientacao.setPlainText("")
        self.thread.start()


    def orientacao(self):
        procedimento = self.box_procedimento.currentText()
        if procedimento == "Orientação":
            self.plainText_orientacao.setEnabled(True)
        else:
            self.plainText_orientacao.setEnabled(False)

    def configuracao(self):
        tipo_nota = self.box_tipo_nota.currentText()
        if tipo_nota == "Fechamento Usário":
            self.input_ocorrencia.setEnabled(True)
            self.box_procedimento.setEnabled(True)
            self.orientacao()

        elif tipo_nota == "Agendamento" or tipo_nota == "Improcedente":
            self.input_ocorrencia.setEnabled(False)
            self.box_procedimento.setEnabled(False)
            self.plainText_orientacao.setEnabled(False)

    # Função processo paralelo
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
    widget=FrmFechamento()
    widget.show()
    sys.exit(app.exec())