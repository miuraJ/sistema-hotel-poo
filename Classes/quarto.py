from __future__ import annotations # Importa annotations para suporte a tipagem

class Quarto:
    # Variável de classe compartilhada por todas as instâncias
    _contador_id: int = 0
    
    def __init__(self, tipo: str = "padrão"):
        # Validadores antes do autoincremento
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("O tipo deve ser uma string não vazia.")
        
        # ID autoincrementado
        Quarto._contador_id += 1

        # Atributos da classe 
        self.__numero: int = Quarto._contador_id # É o próprio ID do quarto
        self.__tipo: str = tipo
        self.__disponivel: bool = True
    
    def reservar(self) -> None:
        self.__disponivel = False

    def liberar(self) -> None:
        self.__disponivel = True

    def estaDisponivel(self) -> bool:
        return self.__disponivel

    # Getters em snake_case
    def get_numero(self) -> int:
        return self.__numero
    
    def get_tipo(self) -> str:
        return self.__tipo