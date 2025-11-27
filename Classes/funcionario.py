from __future__ import annotations  # Importa annotations para suporte a tipagem
from .pessoa import Pessoa
from .hotel import Hotel
from .quarto import Quarto
from .hospede import Hospede
from .reserva import Reserva


class Funcionario(Pessoa):
    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)

    def add_quarto(self, hotel: Hotel, quarto: Quarto) -> bool:
        print("Registrando quarto...")  # Feedback ao usuário para motivos didáticos

        if hotel.add_quarto(quarto):
            print(
                "Quarto registrado com sucesso."
            )  # Feedback ao usuário para motivos didáticos
            return True
        print(
            "Quarto já registrado. Não é possível registrar novamente"
        )  # Feedback ao usuário para motivos didáticos
        return False

    def remover_quarto(self, hotel: Hotel, quarto: Quarto) -> bool:
        print("Removendo quarto...")  # Feedback ao usuário para motivos didáticos

        if hotel.remover_quarto(quarto):
            print(
                "Quarto removido com sucesso."
            )  # Feedback ao usuário para motivos didáticos
            return True
        print(
            "Quarto não encontrado. Não é possível remover."
        )  # Feedback ao usuário para motivos didáticos
        return False

    def registrar_hospede(self, hotel: Hotel, hospede: Hospede) -> bool:
        print(
            "Funcionário registrando hóspede..."
        )  # Feedback ao usuário para motivos didáticos

        if hotel.registrar_hospede(hospede):
            print(
                "Funcionário registrou hóspede com sucesso."
            )  # Feedback ao usuário para motivos didáticos
            return True
        print(
            "Funcionário não encontrou hóspede. Não é possível registrar novamente"
        )  # Feedback ao usuário para motivos didáticos
        return False

    def cancelar_reserva(self, hotel: Hotel, reserva: Reserva) -> bool:
        print(
            "Funcionário cancelando reserva..."
        )  # Feedback ao usuário para motivos didáticos

        nome_hospede = reserva.get_hospede().get_nome()
        for hospede in hotel.get_hospedes():
            if hospede.get_nome() == nome_hospede:
                if hospede.cancelar_reserva(hotel, reserva):
                    print(
                        f"Funcionário cancelou a reserva com sucesso para o hóspede {nome_hospede}."
                    )  # Feedback ao usuário para motivos didáticos
                    return True
        print(
            "Funcionário não encontrou a reserva. Não é possível cancelar."
        )  # Feedback ao usuário para motivos didáticos
        return False

    def listar_quartos(self, hotel: Hotel) -> set:
        return hotel.get_quartos()

    def listar_hospedes(self, hotel: Hotel) -> list:
        return hotel.get_hospedes()

    def listar_reservas(self, hotel: Hotel) -> set:
        return hotel.get_reservas()
