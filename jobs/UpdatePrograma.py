from PyQt5.QtCore import QObject, pyqtSignal
import time, subprocess



class UpdatePrograma(QObject):
    atualiar_software = pyqtSignal()
    erro_update = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)

    def verifica_se_tem_que_atualizar(self):
        while True:
            try:
                print('verificando atualização...')
                servidor = "\\\\DF0000SR207\log\ServiceDesk\Programas\SCCM"
                local = "'C:\Program Files (x86)\Service Desk\SCCM'"
                atualizar = "\\\\DF0000SR207\log\ServiceDesk\Programas\SCCM\BIN\\Update\\Update_SCCM.ps1"
                executavel = "'C:\Program Files (x86)\Service Desk\SCCM\SCCM_Relatorios.exe'"

                comando = (
                        'C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe -Command "&{%s %s %s %s}"' %
                        (atualizar, servidor, local, executavel)

                )
                print(comando)
                print (subprocess.check_call(comando, shell=True))

            except Exception as e:
                e = str(e)
                with open('erro_update.txt', 'a') as f:
                    f.write(e)
                    f.close()

            time.sleep(1200)

