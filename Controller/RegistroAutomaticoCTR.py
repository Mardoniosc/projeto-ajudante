#coding: utf-8
from Model.DTO.RegistroAutomaticoDTO import RegistroAutomaticoDTO
from Model.DAO.RegistroAutomaticoDAO import RegistroAutomaticoDAO

class RegistroAutomaticoCTR:
    @staticmethod
    def registrarChamado(data_registro, atendente, chamado, problema,
                         status, nome_logico, vip, critico, hora_registro):
        registroDTO = RegistroAutomaticoDTO
        registroDTO.Data_registro = data_registro
        registroDTO.Atendente = atendente
        registroDTO.Chamado = chamado
        registroDTO.Problema = problema
        registroDTO.Status = status
        registroDTO.Nome_logico = nome_logico
        registroDTO.Vip = vip
        registroDTO.Critico = critico
        registroDTO.Hora_registro = hora_registro

        registroDAO = RegistroAutomaticoDAO
        resultado = registroDAO.registrar_chamado(registroDTO)
        return resultado