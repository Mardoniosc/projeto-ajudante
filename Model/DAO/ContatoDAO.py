NOTAS = "\\\\DF7562NT713\Mardonio$\\Notas"
# NOTAS = "C:\dev\\Notas_Gerador\\Notas"

class ContatoDAO:
    @staticmethod
    def gerar_nota_contato(dados):

        def preenche_dados(dados, nota_preenchimento, codigo='utf-8'):
            #     Abrir arquivo em modo leitura
            with open('%s%s' % (NOTAS, nota_preenchimento), 'r', encoding="%s" % codigo) as fd:
                txt = fd.read()  # Ler todo o arquivo

                txt = txt.replace('UsuarioX', dados.UsuarioContato)
                txt = txt.replace('NumeroX', dados.TentativaNumero)
                txt = txt.replace('TelefoneChamadoX', dados.TelefoneChamado)
                txt = txt.replace('TelefoneOutlookX', dados.TelefoneUnidadeOutlook)
                txt = txt.replace('StatusLyncX', dados.StatusLync)
                txt = txt.replace('FilaX', dados.FilaContato)

                fd.close()
            with open('%s/NotaPadrao.txt' % NOTAS, 'w', encoding="%s" % codigo) as fd:
                fd.write(txt)  # Escrever texto modificado
                fd.close()

        def nota_tentativa_contato(dados):
            local_nota = '/TentativaDeContato/NotaTentativaDeContato.txt'
            preenche_dados(dados,local_nota)

        def nota_terceira_tentativa(dados):
            local_nota = '/TentativaDeContato/NotaTerceiraTentativa.txt'
            preenche_dados(dados, local_nota)

        def nota_indisponibilidade(dados):
            local_nota = '/TentativaDeContato/NotaIndisponibilidadeDoUsuário.txt'
            preenche_dados(dados, local_nota)

        def nota_agendamento(dados):
            local_nota = '/TentativaDeContato/NotaAgendamento.txt'
            preenche_dados(dados, local_nota,codigo='iso-8859-1')

        if dados.TipoContato == 'Tentativa de Contato':
            nota_tentativa_contato(dados)
        elif dados.TipoContato == '3° Tentativa de Contato':
            nota_terceira_tentativa(dados)
        elif dados.TipoContato == 'Indisponibilidade':

            nota_indisponibilidade(dados)
        elif dados.TipoContato == 'Agendamento':
            nota_agendamento(dados)
