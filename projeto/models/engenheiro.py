from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

class Engeneheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea 

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"CREA: {self.crea}"
                )
    
    def salario_final():
        return 4000.00