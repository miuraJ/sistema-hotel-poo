from __future__ import annotations  # Importa annotations para suporte a tipagem
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
