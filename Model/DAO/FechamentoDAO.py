NOTAS = "\\\\DF7562NT713\Mardonio$\\Notas"
# NOTAS = "C:\dev\\Notas_Gerador\\Notas"

class FechamentoDAO:
    # pegar informações


    @staticmethod
    def gerar_nota(dados, tipo="Fechamento Usário"):

        def nota_fechamento(dados):

            # Abrir o arquivo em modo de leitura
            with open('%s/Fechamento/NotaFechamentoPadrão.txt' % NOTAS, 'r', encoding="utf-8") as fd:
                txt = fd.read()  # Ler todo o arquivo

                txt = txt.replace('UsuarioX', dados.Usuario)
                txt = txt.replace('OcorrenciaX', dados.Ocorrencia)
                txt = txt.replace('ProcedimentoX', dados.Procedimento)
                txt = txt.replace('AcompanhamentoX', dados.Acompanhamento)
                txt = txt.replace('FilaX', dados.Fila)

                fd.close()

            # Abrir o arquivo em modo de escrita
            with open('%s/NotaPadrao.txt' % NOTAS, 'w', encoding="utf-8") as fd:
                fd.write(txt)  # Escrever texto modificado
                fd.close()

        def nota_orietacao(dados):
            with open('%s/Fechamento/NotaFechamentoOrientação.txt' % NOTAS, 'r', encoding="utf-8") as fd:
                txt = fd.read()  # Ler todo o arquivo

                txt = txt.replace('UsuarioX', dados.Usuario)
                txt = txt.replace('OcorrenciaX', dados.Ocorrencia)
                txt = txt.replace('ProcedimentoX', dados.Procedimento)
                txt = txt.replace('AcompanhamentoX', dados.Acompanhamento)
                txt = txt.replace('FilaX', dados.Fila)
                txt = txt.replace('OrientacaoX', dados.Orientacao)

                fd.close()

            # Abrir o arquivo em modo de escrita
            with open('%s/NotaPadrao.txt' % NOTAS, 'w', encoding="utf-8") as fd:
                fd.write(txt)  # Escrever texto modificado
                fd.close()

        def nota_agendamento(dados):
            with open('%s/TentativaDeContato/NotaAgendamento.txt' % NOTAS, 'r', encoding="iso-8859-1") as fd:
                txt = fd.read()  # Ler todo o arquivo

                txt = txt.replace('UsuarioX', dados.Usuario)
                txt = txt.replace('FilaX', dados.Fila)

                fd.close()

            # Abrir o arquivo em modo de escrita
            with open('%s/NotaPadrao.txt' % NOTAS, 'w', encoding="utf-8") as fd:
                fd.write(txt)  # Escrever texto modificado
                fd.close()

        def nota_improcedente(dados):
            with open('%s/Fechamento/NotaImprocedente.txt' % NOTAS, 'r', encoding="utf-8") as fd:
                txt = fd.read()  # Ler todo o arquivo

                txt = txt.replace('UsuarioX', dados.Usuario)
                txt = txt.replace('FilaX', dados.Fila)

                fd.close()

            # Abrir o arquivo em modo de escrita
            with open('%s/NotaPadrao.txt' % NOTAS, 'w', encoding="utf-8") as fd:
                fd.write(txt)  # Escrever texto modificado
                fd.close()

        if tipo == "Fechamento Usário":
            nota_fechamento(dados)
        elif tipo == "Fechamento Usário Orientacao":
            nota_orietacao(dados)
        elif tipo == "Agendamento":
            nota_agendamento(dados)
        elif tipo == "Improcedente":
            nota_improcedente(dados)