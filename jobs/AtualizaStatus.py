import time
from PyQt5.QtCore import QObject, pyqtSignal

class AtualizaStatus(QObject):
    status_sinal = pyqtSignal()
    finished2 = pyqtSignal()


    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def emite_status_sinal(self):
        while True:
            with open('outfile.txt', 'r') as f:
                lines = f.read().splitlines()
                last_line = lines[-1]
                self.status_sinal.emit()

            if last_line.__contains__('Tempo total'):
                print(last_line)
                self.status_sinal.emit()
                self.finished2.emit()

                break

            time.sleep(1)

