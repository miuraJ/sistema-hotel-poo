from __future__ import annotations # Importa annotations para suporte a tipagem
from typing import TYPE_CHECKING
# Imports condicionais - só acontecem para checagem de tipos
if TYPE_CHECKING:
    from .quarto import Quarto
    from .hospede import Hospede

class Reserva:
    def __init__(self, hospede: Hospede, quarto: Quarto):
        self.__hospede: Hospede = hospede
        self.__quarto: Quarto = quarto

    # Getters em snake_case para evitar conflito com os atributos privados
    def get_hospede(self) -> Hospede:
        return self.__hospede

    def get_quarto(self) -> Quarto:
        return self.__quarto