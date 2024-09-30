import os
from projeto.models.endereco import Endereco
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self.verificar_nome(nome)
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def verificar_nome(self, valor):
        self.verificar_nome_tipo_invalido(valor)
        self.verificar_nome_vazio_invalido(valor)

        self.nome = valor 
        return self.nome
    
    def verificar_telefone(self, valor):
        self.verificar_telefone_tipo_invalido(valor)
        self.verificar_telefone_vazio_invalido(valor)

        self.telefone = valor 
        return self.telefone
    
    def verificar_email(self, valor):
        self.verificar_email_tipo_invalido(valor)
        self.verificar_email_vazio_invalido(valor)

        self.email = valor 
        return self.email
    
    def verificar_nome_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto!")
        
    def verificar_nome_vazio_invalido(self, valor):
        if not valor.strip():
            raise TypeError("O nome estar vazio!")
        
    def verificar_telefone_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O telefone deve ser um texto!")
        
    def verificar_telefone_vazio_invalido(self, valor):
        if not valor.strip():
            raise TypeError("O telefone estar vazio!")

    def verificar_email_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve ser um texto!")
        
    def verificar_email_vazio_invalido(self, valor):
        if not valor.strip():
            raise TypeError("O email estar vazio!")

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}"
            f"telefone: {self.telefone}"
            f"Email: {self.email}"
            f"Endereco: {self.endereco}"
        )
    @abstractmethod
    def salario_final():
        pass
    
