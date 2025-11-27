from __future__ import annotations # Importa annotations para suporte a tipagem
from .pessoa import Pessoa
from .hotel import Hotel
from .quarto import Quarto
from .hospede import Hospede
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reserva import Reserva

class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)
    
    def add_quarto(self, hotel: Hotel, quarto: Quarto) -> bool:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        
        if not isinstance(quarto, Quarto):
            raise ValueError("O quarto deve ser um objeto do tipo Quarto.")
        
        print("Registrando quarto...")   # Feedback ao usuário para motivos didáticos
        
        if hotel.add_quarto(quarto):
            print("Quarto registrado com sucesso.")   # Feedback ao usuário para motivos didáticos
            return True
        print("Quarto já registrado. Não é possível registrar novamente")   # Feedback ao usuário para motivos didáticos
        return False

    def remover_quarto(self, hotel: Hotel, quarto: Quarto) -> bool:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        
        if not isinstance(quarto, Quarto):
            raise ValueError("O quarto deve ser um objeto do tipo Quarto.")
        
        print("Removendo quarto...")   # Feedback ao usuário para motivos didáticos
        
        if hotel.remover_quarto(quarto):
            print("Quarto removido com sucesso.")   # Feedback ao usuário para motivos didáticos
            return True
        print("Quarto não encontrado. Não é possível remover.")   # Feedback ao usuário para motivos didáticos
        return False

    def registrar_hospede(self, hotel: Hotel, hospede: Hospede) -> bool:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        
        if not isinstance(hospede, Hospede):
            raise ValueError("O hospede deve ser um objeto do tipo Hospede.")
        
        print("Funcionário registrando hóspede...")   # Feedback ao usuário para motivos didáticos
        
        if hotel.registrar_hospede(hospede):
            print("Funcionário registrou hóspede com sucesso.")   # Feedback ao usuário para motivos didáticos
            return True
        print("Funcionário não encontrou hóspede. Não é possível registrar novamente")   # Feedback ao usuário para motivos didáticos
        return False

    def cancelar_reserva(self, hotel: Hotel, reserva: Reserva) -> bool:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        
        if not isinstance(reserva, Reserva):
            raise ValueError("A reserva deve ser um objeto do tipo Reserva.")
        
        print("Funcionário cancelando reserva...")   # Feedback ao usuário para motivos didáticos
        
        if hotel.cancelar_reserva(reserva):
            print("Funcionário cancelou a reserva com sucesso.")   # Feedback ao usuário para motivos didáticos
            return True
        print("Funcionário não encontrou a reserva. Não é possível cancelar.")   # Feedback ao usuário para motivos didáticos
        return False

    def listar_quartos(self, hotel: Hotel) -> set:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        return hotel.get_quartos()

    def listar_hospedes(self, hotel: Hotel) -> list:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        return hotel.get_hospedes()

    def listar_reservas(self, hotel: Hotel) -> set:
        if not isinstance(hotel, Hotel):
            raise ValueError("O hotel deve ser um objeto do tipo Hotel.")
        return hotel.get_reservas()