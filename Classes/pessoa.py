from __future__ import annotations # Importa annotations para suporte a tipagem

class Pessoa:
    # Variável de classe compartilhada por todas as instâncias
    _contador_id: int = 0
    
    def __init__(self, nome: str, email: str):
        # Validacao do nome em string
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        
        # Validacao do email em string
        if not isinstance(email, str) or '@' not in email:
            raise ValueError("O email deve ser uma string válida com @.")
        
        # ID autoincrementado
        Pessoa._contador_id += 1
        
        # Atributos da classe 
        self.__id: int = Pessoa._contador_id
        self.__nome: str = nome
        self.__email: str = email
    
    # Getters em snake_case
    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email