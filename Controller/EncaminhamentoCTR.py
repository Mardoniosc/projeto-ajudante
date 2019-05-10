# coding: utf-8

from Model.DTO.EncaminhamentoDTO import EncaminhamentoDTO
from Model.DAO.EncaminhamentoDAO import EncaminhamentoDAO

class EncaminhamentoCTR:

    @staticmethod
    def nota_encaminhamento(problema, diagnostico, procedimento_realizado, msg_erro,
                            momento_msg_erro, motivo, imagem, fila, tipo_nota):
        encaminhamentoDTO = EncaminhamentoDTO
        encaminhamentoDTO.Problema = problema
        encaminhamentoDTO.Diagnostico = diagnostico
        encaminhamentoDTO.Procedimento_realizado = procedimento_realizado
        encaminhamentoDTO.Msg_erro = msg_erro
        encaminhamentoDTO.Momento_msg_erro = momento_msg_erro
        encaminhamentoDTO.Motivo = motivo
        encaminhamentoDTO.Imagem = imagem
        encaminhamentoDTO.Fila = fila
        encaminhamentoDTO.TipoNota = tipo_nota

        encaminhamentoDAO = EncaminhamentoDAO
        encaminhamentoDAO.gerar_nota_contato(encaminhamentoDTO)