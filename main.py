from Classes.funcionario import Funcionario
from Classes.hospede import Hospede
from Classes.hotel import Hotel
from Classes.quarto import Quarto

AUTOR = "Inácio Miura"
SEPARADOR = "=" * 50


def exibir_cabecalho():
    """Exibe o cabeçalho do sistema."""
    print(f"\n{SEPARADOR}")
    print("Hotel POO - Sistema de Gestão")
    print(f"Desenvolvido por {AUTOR}")
    print(f"{SEPARADOR}\n")


def menu_principal():
    """Menu principal - escolha de perfil."""
    print("SELECIONE O PERFIL DE ACESSO:\n")
    print("1. Funcionário")
    print("2. Hóspede")
    print("0. Sair do Sistema\n")
    return input("Escolha uma opção: ").strip()


def menu_funcionario():
    """Menu específico para operações do funcionário."""
    print(f"\n{SEPARADOR}")
    print("MENU FUNCIONÁRIO")
    print(SEPARADOR)
    print("1. Registrar quarto")
    print("2. Remover quarto")
    print("3. Registrar hóspede")
    print("4. Cancelar reserva")
    print("0. Voltar ao menu principal\n")
    return input("Escolha uma opção: ").strip()


def menu_hospede(hospede: Hospede):
    """Menu específico para operações do hóspede."""
    print(f"\n{SEPARADOR}")
    print(f"MENU DO HÓSPEDE {hospede.get_nome()}")
    print(SEPARADOR)
    print("1. Fazer reserva")
    print("2. Cancelar reserva")
    print("3. Consultar minhas reservas")
    print("0. Voltar ao menu principal\n")
    return input("Escolha uma opção: ").strip()


# === FLUXOS DO FUNCIONÁRIO ===


def fluxo_registrar_quarto(funcionario: Funcionario, hotel: Hotel):
    """Fluxo completo para registrar um quarto."""
    print(f"\n{SEPARADOR}")
    print("REGISTRAR QUARTO")
    print(SEPARADOR)
    tipo = input("Digite o tipo do quarto (ou Enter para 'standard'): ").strip()

    try:
        quarto = Quarto(tipo) if tipo else Quarto()
        if funcionario.add_quarto(hotel, quarto):
            print(f"✓ Quarto #{quarto.get_numero()} registrado!")
        else:
            print("✗ Quarto já existe.")
    except ValueError as e:
        print(f"✗ Erro: {e}")


def fluxo_remover_quarto(funcionario: Funcionario, hotel: Hotel):
    print(f"\n{SEPARADOR}")
    print("REMOVER QUARTO")
    print(SEPARADOR)

    quartos = funcionario.listar_quartos(hotel)
    if not quartos:
        print("Não há quartos para remover.")
        return

    print("Quartos disponíveis:")
    for quarto in quartos:
        print(f"Quarto #{quarto.get_numero()} - Tipo: {quarto.get_tipo()}")

    try:
        numero = int(
            input(
                "Digite o NÚMERO do quarto para remover, ou 0 para cancelar: "
            ).strip()
        )
    except ValueError:
        print("✗ Número inválido!")
        return

    if numero == 0:
        return

    # Buscar o quarto pelo número
    quarto_encontrado = None
    for quarto in quartos:
        if quarto.get_numero() == numero:
            quarto_encontrado = quarto
            break

    if not quarto_encontrado:
        print(f"✗ Quarto #{numero} não encontrado.")
        return

    if funcionario.remover_quarto(hotel, quarto_encontrado):
        print(f"✓ Quarto #{numero} removido!")
    else:
        print("✗ Erro ao remover quarto.")


def fluxo_registrar_hospede(funcionario: Funcionario, hotel: Hotel):
    """Fluxo completo para registrar um hóspede."""
    print(f"\n{SEPARADOR}")
    print("REGISTRAR HÓSPEDE")
    print(SEPARADOR)
    nome = input("Nome do hóspede: ").strip()
    email = input("Email do hóspede: ").strip()

    try:
        hospede = Hospede(nome, email)
        funcionario.registrar_hospede(hotel, hospede)
    except ValueError as e:
        print(f"✗ Erro: {e}")


def fluxo_cancelar_reserva_funcionario(funcionario: Funcionario, hotel: Hotel):
    """Fluxo para funcionário cancelar uma reserva."""
    print(f"\n{SEPARADOR}")
    print("CANCELAR RESERVA")
    print(SEPARADOR)
    
    reservas = list(funcionario.listar_reservas(hotel))
    
    if not reservas:
        print("Não há reservas para cancelar.")
        return
    
    for i, reserva in enumerate(reservas, 1):
        quarto = reserva.get_quarto()
        print(f"{i}. Quarto #{quarto.get_numero()} - Tipo: {quarto.get_tipo()} - Hospede: {reserva.get_hospede().get_nome()}")
    
    numero = input(
        "Digite o número da reserva para cancelar, ou 0 para cancelar: "
    ).strip()
    
    if numero == "0":
        return
    
    reserva = reservas[int(numero) - 1]
    
    if funcionario.cancelar_reserva(hotel, reserva):
        print(f"✓ Reserva #{numero} cancelada!")
    else:
        print("✗ Erro ao cancelar reserva.")


# === FLUXOS DO HÓSPEDE ===
def mensagem_sem_hospedes():
    print("✗ Não há hóspedes cadastrados.")
    print("Cadastre um hóspede primeiro")
    print(f"\n{SEPARADOR}")
    return


def terminal_busca_hospede(hotel: Hotel) -> Hospede | None:
    nome = input("Digite o nome do hóspede: ").strip()

    for hospede in hotel.get_hospedes():
        if hospede.get_nome() == nome:
            print(f"✓ Hóspede '{nome}' encontrado.")
            print(f"\n{SEPARADOR}")
            return hospede
    print(f"✗ Hóspede '{nome}' não encontrado.")
    print(f"\n{SEPARADOR}")
    return None


def buscar_hospede_por_nome(hotel: Hotel, nome: str) -> Hospede | None:
    for hospede in hotel.get_hospedes():
        if hospede.get_nome() == nome:
            return hospede
    return None


def fluxo_fazer_reserva(hospede: Hospede, hotel: Hotel):
    """Fluxo completo para hóspede fazer reserva."""
    print(f"\n{SEPARADOR}")
    print("FAZER RESERVA")
    print(SEPARADOR)
    hospede.fazer_reserva(hotel)


def fluxo_cancelar_reserva_hospede(hospede: Hospede, hotel: Hotel):
    """Fluxo para hóspede cancelar sua reserva."""
    print(f"\n{SEPARADOR}")
    print("CANCELAR RESERVA")
    print(SEPARADOR)
    reservas = hospede.consultar_reservas()

    if not reservas:
        print("Você não tem reservas para cancelar.")
        return

    for i, reserva in enumerate(reservas, 1):
        quarto = reserva.get_quarto()
        print(f"{i}. Quarto #{quarto.get_numero()} - Tipo: {quarto.get_tipo()} - Hospede: {reserva.get_hospede().get_nome()}")

    numero = input(
        "Digite o número da reserva para cancelar, ou 0 para cancelar: "
    ).strip()

    if numero == "0":
        return

    reserva = reservas[int(numero) - 1]

    if hospede.cancelar_reserva(hotel, reserva):
        print(f"✓ Reserva #{numero} cancelada!")
    else:
        print(f"✗ Reserva #{numero} não encontrada.")


def fluxo_consultar_reservas(hospede: Hospede):
    """Fluxo para hóspede consultar suas reservas."""
    print(f"\n{SEPARADOR}")
    print("MINHAS RESERVAS")
    print(SEPARADOR)
    reservas = hospede.consultar_reservas()

    if not reservas:
        print("Você não possui reservas.")
    else:
        for i, reserva in enumerate(reservas, 1):
            quarto = reserva.get_quarto()
            print(f"{i}. Quarto #{quarto.get_numero()} - Tipo: {quarto.get_tipo()} - Hospede: {reserva.get_hospede().get_nome()}")


# === LOOPS DE MENU ===


def loop_menu_funcionario(funcionario: Funcionario, hotel: Hotel):
    """Loop do menu do funcionário."""
    while True:
        opcao = menu_funcionario()

        if opcao == "1":
            fluxo_registrar_quarto(funcionario, hotel)
        elif opcao == "2":
            fluxo_remover_quarto(funcionario, hotel)
        elif opcao == "3":
            fluxo_registrar_hospede(funcionario, hotel)
        elif opcao == "4":
            fluxo_cancelar_reserva_funcionario(funcionario, hotel)
        elif opcao == "0":
            break
        else:
            print("✗ Opção inválida!")


def loop_menu_hospede(hospede: Hospede, hotel: Hotel):
    """Loop do menu do hóspede."""
    while True:
        opcao = menu_hospede(hospede)

        if opcao == "1":
            fluxo_fazer_reserva(hospede, hotel)
        elif opcao == "2":
            fluxo_cancelar_reserva_hospede(hospede, hotel)
        elif opcao == "3":
            fluxo_consultar_reservas(hospede)
        elif opcao == "0":
            break
        else:
            print("✗ Opção inválida!")


# === MAIN ===


def main():
    """Função principal do sistema."""
    exibir_cabecalho()

    # Inicialização
    hotel = Hotel()
    funcionario = Funcionario("Admin", "admin@hotel.com")
    # hospede = Hospede("Cliente Exemplo", "cliente@email.com")

    # Loop principal
    while True:
        opcao = menu_principal()

        if opcao == "1":
            loop_menu_funcionario(funcionario, hotel)
        elif opcao == "2":
            if not hotel.get_hospedes():
                mensagem_sem_hospedes()
            else:
                hospede = terminal_busca_hospede(hotel)
                if hospede:
                    loop_menu_hospede(hospede, hotel)
        elif opcao == "0":
            print("\nEncerrando sistema... Até logo!")
            break
        else:
            print("✗ Opção inválida!")


if __name__ == "__main__":
    main()

