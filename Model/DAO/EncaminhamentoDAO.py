# coding: utf-8
NOTAS = "\\\\DF7562NT713\Mardonio$\\Notas"

class EncaminhamentoDAO:
    @staticmethod
    def gerar_nota_contato(dados):

        def preenche_dados(dados, nota_preenchimento, codigo='utf-8'):
            #     Abrir arquivo em modo leitura
            with open('%s%s' % (NOTAS, nota_preenchimento), 'r', encoding="%s" % codigo) as fd:
                txt = fd.read()  # Ler todo o arquivo
                # txt = "NomeEquipeX de alguma coisa pardada FilaX quero ver como fica"
                txt = txt.replace('NomeEquipeX', dados.TipoNota)
                txt = txt.replace('ResumoX', dados.Problema)
                txt = txt.replace('DiagnosticoX', dados.Diagnostico)
                txt = txt.replace('ProceimentoX', dados.Procedimento_realizado)
                if (dados.Msg_erro == ''):
                    txt = txt.replace('\n3.1 - Mensagem de erro(se houver):\n', "3.1 Sem mensagem de erro")
                    txt = txt.replace('\n3.2 - Momento em que ocorre(se houver):\n', "")
                txt = txt.replace('MensagemErroX', dados.Msg_erro)
                txt = txt.replace('MomentoOcorreX', dados.Momento_msg_erro)
                if (dados.Imagem=='Não'):
                    txt = txt.replace('\n4.1 - Segue anexo print do erro.\n', '')
                txt = txt.replace('MotivoX', dados.Motivo)
                txt = txt.replace('FilaX', dados.Fila)


                fd.close()

            with open('%s/NotaPadrao.txt' % NOTAS, 'w', encoding="%s" % codigo) as fd:
                fd.write(txt)  # Escrever texto modificado
                fd.close()

        def encaminhamento_caixa(dados):
            local_nota = '/Encaminhamento/encaminhamento_padrao.txt'
            preenche_dados(dados, local_nota, codigo='iso-8859-1')

        def encaminhamento_externo(dados):
            local_nota = '/Encaminhamento/encaminhamento_padrao.txt'
            preenche_dados(dados, local_nota, codigo='iso-8859-1')

        def encaminhamento_incidentes(dados):
            local_nota = '/Encaminhamento/incidentes.txt'
            preenche_dados(dados, local_nota, codigo='iso-8859-1')

        if dados.TipoNota == 'Equipe Caixa':
            encaminhamento_caixa(dados)

        elif dados.TipoNota == 'Equipe Incidentes':
            encaminhamento_incidentes(dados)

        elif dados.TipoNota == 'Equipe Externo':
            encaminhamento_externo(dados)



