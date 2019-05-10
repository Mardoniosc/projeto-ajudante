# coding: utf-8

from Model.DTO.FechamentoDTO import FechamentoDTO
from Model.DAO.FechamentoDAO import FechamentoDAO

class FechamentoCTR:
    @staticmethod
    def nota_fechamento(usuario, ocorrencia, procedimento, fila, acompanhamento, orientacao, tipo_de_nota):

        fechamentoDTO = FechamentoDTO
        fechamentoDTO.Usuario = usuario
        fechamentoDTO.Ocorrencia = ocorrencia
        fechamentoDTO.Procedimento = procedimento
        fechamentoDTO.Fila = fila
        fechamentoDTO.Acompanhamento = acompanhamento
        fechamentoDTO.Orientacao = orientacao
        fechamentoDTO.TipoNota = tipo_de_nota

        fechamentoDAO = FechamentoDAO

        if tipo_de_nota == "Fechamento Usário":
            if orientacao != "":
                # nota de orientação
                tipo_de_nota = "Fechamento Usário Orientacao"
                fechamentoDAO.gerar_nota(fechamentoDTO,tipo_de_nota)
            else:
                # nota de fechamento
                fechamentoDAO.gerar_nota(fechamentoDTO,tipo_de_nota)
        else:
            fechamentoDAO.gerar_nota(fechamentoDTO, tipo_de_nota)
