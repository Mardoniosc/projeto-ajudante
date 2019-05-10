# coding: utf-8
import sys, os, subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.uic import loadUi
from Controller.ContatoCTR import TentativaDeContatoCTR
NOTAS = "\\\\DF7562NT713\Mardonio$\\Notas"
# NOTAS = "C:\dev\\Notas_Gerador\\Notas"




class FrmTentativaDeContato(QWidget):
    def __init__(self):
        super(FrmTentativaDeContato, self).__init__()
        loadUi('view/UI/FrmTentativaDeContato.ui', self)
        self.setWindowTitle('Tentativa de Contato')

        self.thread = QThread()
        self.notapadra = AbrirNotaPadrao()

        self.notapadra.moveToThread(self.thread)
        self.thread.started.connect(self.notapadra.abrirNotaPadrao)

        self.notapadra.finished.connect(self.fim_do_processo_paralelo)


        # Botões aba Tentativa de Contato
        self.button_gerar_nota_contato.clicked.connect(self.gerar_nota_contato)

    def gerar_nota_contato(self):
        tipo_nota = self.box_tipo_nota_contato.currentText()
        usuario = self.input_usuario_contato.text()

        if self.radio_1.isChecked():
            tentativa_numero = "1"
        elif self.radio_2.isChecked():
            tentativa_numero = "2"
        else:
            tentativa_numero = "3"

        telefone_chamado = self.input_telefone_chamado.text()
        telefone_catalogo = self.input_telefone_catalogo.text()
        status_lync = self.box_status_lync.currentText()
        fila = self.box_fila_contato.currentText()

        TentativaDeContatoCTR.nota_tentativa_de_contato(usuario,telefone_chamado,telefone_catalogo,fila,status_lync,tentativa_numero, tipo_nota)

        # self.input_usuario.setText("")
        # self.input_ocorrencia.setText("")
        # self.plainText_orientacao.setPlainText("")
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
    widget=FrmTentativaDeContato()
    widget.show()
    sys.exit(app.exec())