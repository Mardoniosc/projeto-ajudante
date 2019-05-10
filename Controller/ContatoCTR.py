# coding: utf-8

from Model.DTO.ContatoDTO import ContatoDTO
from Model.DAO.ContatoDAO import ContatoDAO

class TentativaDeContatoCTR:

    @staticmethod
    def nota_tentativa_de_contato(usuario, telefone_chamado, telefone_catalogo, fila, status_lync,
                                  tentativa_numero, tipo_nota):
        contatoDTO = ContatoDTO

        contatoDTO.UsuarioContato = usuario
        contatoDTO.TelefoneChamado = telefone_chamado
        contatoDTO.TelefoneUnidadeOutlook = telefone_catalogo
        contatoDTO.FilaContato = fila
        contatoDTO.StatusLync = status_lync
        contatoDTO.TentativaNumero = tentativa_numero
        contatoDTO.TipoContato = tipo_nota

        contatoDAO = ContatoDAO

        contatoDAO.gerar_nota_contato(contatoDTO)