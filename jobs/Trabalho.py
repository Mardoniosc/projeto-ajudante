from PyQt5.QtCore import QObject, pyqtSignal
import subprocess

class Trabalho(QObject):
    sinal_log_status = pyqtSignal()
    finished = pyqtSignal()
    erro_geracao_relatorio = pyqtSignal()


    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def guardar_usuario_e_senha(self, contaP, senhaP):
        global usuario
        global senha

        usuario = contaP
        senha = senhaP



    def executa_outro_processo(self):


        with open('CGC_.txt', 'r') as arq:
            CGC = arq.readline()
            arq.close()

        def gerar_relatorio_geral(usuario, senha, CGC_):
            try:

                caminho = "'C:\Program Files (x86)\Service Desk\SCCM\BIN\Process\SCCM.ps1'"
                local = "'C:\Program Files (x86)\Service Desk\SCCM'"

                comando = (
                        'C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe -Command "&{.%s %s %s %s %s}"' %
                        (caminho, local, usuario, senha, CGC_)
                )

                print(comando)
                out_file = open('outfile.txt', 'a')
                subprocess.check_call(comando, shell=True, stdout=out_file)
                out_file.close()

                return True
            except Exception as e:
                e = str(e)
                with open('erro_relatorio.txt', 'a') as f:
                    f.write(e)
                    f.close()
                return False

        relatorio = gerar_relatorio_geral (usuario, senha, CGC)
        if relatorio == True:
            self.finished.emit()
        else:
            self.erro_geracao_relatorio.emit()