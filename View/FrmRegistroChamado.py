
import sys, subprocess
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.uic import loadUi

class FrmRegistroChamado(QWidget):
    def __init__(self):
        super(FrmRegistroChamado, self).__init__()
        loadUi('view/UI/FrmRegistroDeChamados.ui', self)
        self.setWindowTitle('Registro de Chamados')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmRegistroChamado()
    widget.show()
    sys.exit(app.exec())

