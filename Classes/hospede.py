from __future__ import annotations # Importa annotations para suporte a tipagem
from .pessoa import Pessoa
from .reserva import Reserva
from typing import TYPE_CHECKING
# Imports condicionais - só acontecem para checagem de tipos
if TYPE_CHECKING:
    from .hotel import Hotel
    
class Hospede(Pessoa):
    def __init__(self, nome: str, email: str):
        self.__reservas: list = list()
        super().__init__(nome, email)
    
    def fazer_reserva(self, hotel: Hotel) -> bool:
        # Modifiquei a lógica pois, seguindo o UML recebido, não fazia sentido
        # o cliente receber um objeto reserva que ainda não existia. Também,
        # não seria coerente instanciar uma reserva sem ser por um método da
        # classe Hotel.

        # Validação do hotel
        # if not isinstance(hotel, Hotel):
        #     raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        
        reserva = hotel.registrar_reserva(self)

        # Feedback ao usuário para motivos didáticos
        if reserva:
            print("Reserva feita com sucesso.")
            self.__reservas.append(reserva)
            return True
        else:
            print("Não foi possível fazer a reserva.")
            return False
    
    def cancelar_reserva(self, hotel: Hotel, reserva: Reserva) -> bool:
        # Modifiquei a lógica pois não é possível cancelar uma reserva sem
        # modificar o objeto hotel, que é o responsável por gerenciar as
        # reservas.

        # Validações
        # if not isinstance(hotel, Hotel):
        #     raise ValueError("O hotel deve ser um objeto do tipo Hotel.")

        if not isinstance(reserva, Reserva):
            raise ValueError("A reserva deve ser um objeto do tipo Reserva.")

        cancelamento = hotel.cancelar_reserva(reserva)

        # Feedback ao usuário para motivos didáticos
        if cancelamento:
            print("Reserva cancelada com sucesso.")
            self.__reservas.remove(reserva)
        else:
            print("Não foi possível cancelar a reserva.")
        return cancelamento

    def consultar_reservas(self) -> list:
        # Feedback ao usuário para motivos didáticos
        print("Consultando reservas...")
        return self.__reservas