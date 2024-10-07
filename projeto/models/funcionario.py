import os
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo) -> None:
        self.nome = self.verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.sexo = sexo

    def verificar_nome(self, valor):
        self.verificar_nome_tipo_invalido(valor)
        self.verificar_nome_vazio_invalido(valor)

        self.nome = valor 
        return self.nome
    
    def verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto!")
        
    def verificar_nome_vazio_invalido(self, valor):
        if not valor.strip():
            raise TypeError("O nome estar vazio!")
        

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"telefone: {self.telefone}"
            f"Email: {self.email}"
            f"Endereco: {self.endereco}"
            f"Sexo: {self.sexo}"
        )
    @abstractmethod
    def salario_final():
        pass
    
