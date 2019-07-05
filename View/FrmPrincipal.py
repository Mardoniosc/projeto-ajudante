""".NOTES
    ===========================================================================
    Created on:   	26/04//2019
    Created by:   	p772920 - Mardonio Silva da Costa
    Organization: 	Caixa Econômica Federal / Stefanini
    Filename:     	FrmPrincipal.py
    ===========================================================================
    .DESCRIPTION
        Arquivo principal de controle do sistema.
    .UPDATES
        03/05/2019 - P772920 - Adicionado novas view.
"""

from .FrmLogin import *
from Diversos.recursos import *
from .FrmFechamento import FrmFechamento
from .FrmTentativaDeContato import FrmTentativaDeContato
from .FrmEncaminhamento import FrmEncaminhamento
from .FrmRegistroChamado import FrmRegistroChamado

class FrmPrincipal(QMainWindow):
    def __init__(self):
        super(FrmPrincipal, self).__init__()
        loadUi('view/UI/FrmPrincipal.ui', self)
        dados = self.pega_usuario_senha()
        global usuarioP
        global senhaP
        usuarioP = dados[0]
        senhaP = dados[1]

        usuario_logado = self.pega_nome_usuario_logado(usuarioP)
        self.label_nome_usurio.setText(usuario_logado)
        #     Botões do menu Arquivo

        # SubMenu Registro de chamados
        self.actionRegistrar_Chamado.triggered.connect(self.click_registrar_chamados)

        #SubMenu Gerador de notas
        self.actionFechamento.triggered.connect(self.click_fechamento)
        self.actionEncaminhamento.triggered.connect(self.click_encaminhamento)
        self.actionTentativa_de_Contato.triggered.connect(self.click_tentativadecontato)


        # SubMenu Login
        self.actionEsta_o_de_Trabalho.triggered.connect(self.estacao_trabalho_login)
        self.actionCofre_Recilclador.triggered.connect(self.estacao_trabalho_login)
        self.actionEsta_o_de_Captura.triggered.connect(self.estacao_captura_login)
        self.actionEstal_ao_Financeira.triggered.connect(self.estacao_financeira_login)


        self.actionSair.triggered.connect(self.click_sair)
        # Body

        self.checkBox_diferente.toggled.connect(lambda: self.diferente())
    @staticmethod
    def pega_nome_usuario_logado(matricula):

        comando_verifica_nome = ("net user /domain %s | FIND /I \"Nome Completo\"" % (matricula))
        try:
            nome_atendente = str(subprocess.check_output(comando_verifica_nome, shell=True))
        except:
            return False
        nome = str(nome_atendente[38:])
        nome_sobrenome = (nome.split('\\r\\n'))
        nome_sobrenome = (nome_sobrenome[0].split(' - CETEC'))
        nome_a_mostrar_guardar = (nome_sobrenome[0])
        return nome_a_mostrar_guardar



    def diferente(self):
        if self.checkBox_diferente.isChecked():
            self.lineEdit_senha.setEnabled(True)
            return True
        else:
            self.lineEdit_senha.setEnabled(False)
            return False


        ######################################  SUBMENU LOGIN   ###########################################

    def estacao_financeira_login(self):
        print('logando na EF')
        nome_logico = QInputDialog.getText(None, 'Nome logico', 'Digite o nome logico')
        estacao = nome_logico[0]
        conectarnaEF(estacao,usuario=usuarioP, senha=senhaP)

    def estacao_trabalho_login(self):
        resultado = self.diferente()
        if resultado == True:
            senhaA = self.lineEdit_senha.text()
            usuario = usuarioP
            usuario = "A" + usuario[1:]
            nome_logico = QInputDialog.getText(None, 'Nome logico', 'Digite o nome logico')
            estacao = nome_logico[0]
            conexao_remota(estacao, usuario, senhaA)

        else:
            usuario = usuarioP
            usuario = "A" + usuario[1:]
            nome_logico = QInputDialog.getText(None, 'Nome logico','Digite o nome logico')
            estacao = nome_logico[0]
            conexao_remota(estacao, usuario, senhaP)

    def estacao_captura_login(self):
        nome_logico = QInputDialog.getText(None, 'Nome logico', 'Digite o nome logico')
        estacao = nome_logico[0]
        print(estacao)
        conectarnaEC(estacao)

    def pega_usuario_senha(self):
        with open('./Diversos/security/pass.txt','r') as pw:
            dados = (pw.readline())
            pw.close()
        dados = dados.split(';')
        return dados

        ############################  SUBMENU REGISTRA DE CHAMADOS   ###############################

    def click_registrar_chamados(self):
        self.frmregistrochamados = QMainWindow()
        self.widget = FrmRegistroChamado()
        self.widget.show()

        ############################  SUBMENU GERAR NOTAS   ###############################

    def click_fechamento(self):
        self.frmfechamento = QMainWindow()
        self.widget = FrmFechamento()
        self.widget.show()

    def click_encaminhamento(self):
        self.frmencaminhamento = QMainWindow()
        self.widget = FrmEncaminhamento()
        self.widget.show()

    def click_tentativadecontato(self):
        self.frmtentativadecontato = QMainWindow()
        self.widget = FrmTentativaDeContato()
        self.widget.show()

        ######################################  SUBMENU SAIR   ###########################################

    def click_sair(self):
        exit()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    widget=FrmPrincipal()
    widget.show()
    sys.exit(app.exec())