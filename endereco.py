import os 
class Endereco():
    def __init__(self,logradouro:str,numero:str,complemtento:str,cep:str,cidade:str) -> None:
        self.logradouro= logradouro
        self.numero= numero
        self.complemento= complemtento
        self.cep= cep
        self.cidade= cidade
    def __str__(self) -> str:
        return (f"\nLogradouro{self.logradouro}\nnumero{self.numero}\ncomplemento{self.complemento}\ncep{self.cep}\ncidade{self.cidade}")
    
        
        
