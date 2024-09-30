from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario



class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm:str,endereco: Endereco) -> None:
        self.crm= crm
        super().__init__(nome, telefone, email, endereco)

    def __str__(self) -> str:
        return super().__str__() + f"\ncrm{self.crm}"
    
    def salario_final():
        return 4500.0
    