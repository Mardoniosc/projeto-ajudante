# coding: utf-8
from Model.DTO.RegistroAutomaticoDTO import RegistroAutomaticoDTO
from Model.DAO.RegistroChamadoDAO import RegistroChamadoDAO

class RegistroChamadoCTR:

    @staticmethod
    def inserrir(data_guardar, atendente, chamado, problema, status, nome_logico, vip,
                                                 critico, hora_guardar):

        registroChamadoDTO = RegistroAutomaticoDTO
        registroChamadoDTO.Data_registro = data_guardar
        registroChamadoDTO.Atendente = atendente
        registroChamadoDTO.Chamado = chamado
        registroChamadoDTO.Problema = problema
        registroChamadoDTO.Status = status
        registroChamadoDTO.Nome_logico = nome_logico
        registroChamadoDTO.Vip = vip
        registroChamadoDTO.Critico = critico
        registroChamadoDTO.Hora_registro = hora_guardar

        registroChamadoDAO = RegistroChamadoDAO

        resultado = registroChamadoDAO.inserir(registroChamadoDTO)
        return resultado
    @staticmethod
    def pesquisar(tipo, atendente, registro):
        registroChamadoDTO = RegistroChamadoDTO
        RegistroChamadoDTO.Atendente = atendente
        RegistroChamadoDTO.Chamado = registro

        # Todos os registros
        if tipo == 1:
            resultado = RegistroChamadoDAO.pesquisar(1, registroChamadoDTO)
            return resultado

        # Todos os registros do usuário
        elif tipo == 2:
            resultado = RegistroChamadoDAO.pesquisar(2, registroChamadoDTO)
            return resultado

        # Todos os registros do usuário em um limite de 100
        elif tipo == 3:
            resultado = RegistroChamadoDAO.pesquisar(3, registroChamadoDTO)
            return resultado

        # Apenas um registro por wo
        elif tipo == 4:
            resultado = RegistroChamadoDAO.pesquisar(4, registroChamadoDTO)
            return resultado
        else:
            return False

    @staticmethod
    def excluir():
        pass

    @staticmethod
    def atualizar():
        pass

# x = RegistroChamadoCTR
# x.inserrir("14/08/1991",'Mardonio','wo000011','algumacoisa','Concluido',
#              'DF7562ET356',0,0,'23:41:45')
#
# x.pesquisar(4,"Mardonio Silva da Costa", "WO0000038181250")

