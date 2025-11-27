from __future__ import annotations  # Importa annotations para suporte a tipagem
from .quarto import Quarto
from .hospede import Hospede
from .reserva import Reserva


# Esta classe viola os princípios de clean code com comentários explicativos por motivos didáticos
class Hotel:
    def __init__(self):
        self.__quartos: set = set()  # Utilizei set para evitar duplicidade
        self.__hospedes: list = list()  # Utilizei list para manter a ordem
        self.__reservas: set = set()  # Utilizei set para evitar duplicidade

    def add_quarto(self, quarto: Quarto) -> bool:
        if quarto not in self.__quartos:
            self.__quartos.add(quarto)
            return True

        return False

    def remover_quarto(self, quarto: Quarto) -> bool:
        if quarto in self.__quartos:
            self.__quartos.remove(quarto)
            return True
        return False

    def registrar_hospede(self, hospede: Hospede) -> bool:
        if hospede not in self.__hospedes:
            self.__hospedes.append(hospede)
            return True
        return False

    def registrar_reserva(self, hospede: Hospede) -> Reserva | None:
        # Criei este método porque considerei importante que o hotel
        # fosse o responsável por registrar a reserva.
        # O hóspede entra em contato direto com o hotel e não com um funcionário.

        # Feedback ao usuário para motivos didáticos
        print("Hotel registrando reserva...")

        # Verifica se há quartos disponíveis
        for quarto in self.__quartos:
            if quarto.estaDisponivel():
                try:
                    quarto.reservar()
                    reserva: Reserva = Reserva(hospede, quarto)
                    self.__reservas.add(reserva)
                    print("Hotel reservou com sucesso.")  # Feedback didático
                    return reserva  # Retorna o objeto reserva
                except Exception as e:  # Captura exceções gerais mas explicita
                    print(f"Erro ao reservar: {e}")  # Feedback didático
                    continue

        # Se chegar aqui, não há quartos disponíveis
        print("Hotel não encontrou quartos disponíveis.")  # Feedback didático
        print("Hotel não pode realizar a reserva.")  # Feedback didático
        return None

    def cancelar_reserva(self, reserva: Reserva) -> bool:
        # Feedback ao usuário para motivos didáticos
        print("Hotel cancelando reserva...")
        try:
            self.__reservas.remove(reserva)
            reserva.get_quarto().liberar()
            print("Hotel cancelou a reserva com sucesso.")  # Feedback didático
            return True
        except KeyError:
            # Feedback ao usuário para motivos didáticos
            print("Hotel não encontrou a reserva. Não é possível cancelar.")
            return False

    # getters
    def get_quartos(self) -> set:
        return self.__quartos

    def get_hospedes(self) -> list:
        return self.__hospedes

    def get_reservas(self) -> set:
        return self.__reservas
