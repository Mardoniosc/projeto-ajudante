from PyQt5.QtCore import QObject, pyqtSignal

class LogarEstacao(QObject):
    logar_estacao = pyqtSignal()
    erro_ao_logar = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def conectando_a_estacao(self):
        pass