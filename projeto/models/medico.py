from projeto.models.enums.sexo import Sexo
from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo,crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, sexo)
        self.crm = crm
    
    def __str__(self) -> str:
        return super().__str__() + f"CRM: {self.crm}"
    
    def _Verifica__nome(self, nome: str) -> str:
        return super()._Verifica__nome(nome)
    
    def salario_final():
        return 4500.0
    