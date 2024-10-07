from projeto.models.enums.UnidadeFederativa import unidade_federativa
class Endereco():
    def __init__(self,logradouro:str,numero:str,complemtento:str,cep:str,cidade:str,  uf: unidade_federativa) -> None:
        self.logradouro= logradouro
        self.numero= numero
        self.complemento= complemtento
        self.cep= cep
        self.cidade= cidade
        self.uf = uf
    def __str__(self) -> str:
        return (f"\nLogradouro{self.logradouro}\nnumero{self.numero}\ncomplemento{self.complemento}\ncep{self.cep}\ncidade{self.cidade}\nUF: {self.uf}")
    
        
        
