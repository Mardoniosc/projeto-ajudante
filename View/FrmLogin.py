# coding: utf-8

import sys, win32security, win32con, getpass
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QDialog, QMessageBox, QInputDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.uic import loadUi
from jobs.Trabalho import Trabalho
from .FrmPrincipal import FrmPrincipal

class FrmLogin(QDialog):
    def __init__(self):
        super(FrmLogin, self).__init__()
        loadUi('View/UI/FrmLogin.ui', self)

        usuario = getpass.getuser()
        usuario = "P" + usuario[1:]
        self.input_usuario.setText(usuario)
        self.buttonBox.accepted.connect(self.accept_click)
        self.buttonBox.rejected.connect(self.reject_click)
    @staticmethod
    def guardar_usuario_e_senha(contaP, senhaP):
        with open('./Diversos/security/pass.txt','w') as pw:
            pw.write(contaP + ';' + senhaP)
            pw.close()


    def autentica_usuario_no_ad(self, userName, senha, dominio):
        try:
            token = win32security.LogonUser(
                userName,
                dominio,
                senha,
                win32con.LOGON32_LOGON_INTERACTIVE,
                win32con.LOGON32_PROVIDER_DEFAULT
            )
            authenticacao = bool(token)

            return authenticacao
        except:
            FrmLogin()
            return False

    def accept_click(self):

        usuario_a = self.input_usuario.text()
        senha_a = self.input_senha.text()

        resultado = self.autentica_usuario_no_ad(usuario_a,  senha_a, 'CORPCAIXA')
        print(resultado)
        if resultado == True:
            self.guardar_usuario_e_senha(usuario_a, senha_a)
            self.frmaluguel = QWidget()
            self.widget = FrmPrincipal()
            self.widget.show()
        else:
            QMessageBox.critical(self, "Login", "Usuário ou senha incorreto!\n"
                                                "tente novamente"),
            self.frmaluguel = QDialog()
            self.widget = FrmLogin()
            self.widget.show()

    def reject_click(self):
        print('reject')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmLogin()
    widget.show()
    sys.exit(app.exec())