from projeto.models.enums.sexo import Sexo
from projeto.models.enums.UnidadeFederativa import unidade_federativa
from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, Sexo: str, unidade_federativa: str, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, Sexo, unidade_federativa)
        self.crea = crea

    def __str__(self) -> str:
        return super().__str__() + f"\nCrea: {self.crea}"
    
    def _Verifica__nome(self, nome: str) -> str:
        return super()._Verifica__nome(nome)

    def salario_final():
        return 4000.00