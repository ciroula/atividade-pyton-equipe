import pytest
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engeneheiro

@pytest.fixture
def criar_engenheiro():
    engenheiro1 = Engeneheiro("Michel","719","Michel@",
                    Endereco("tancredo","25","casa","86615","salvador")
                              )
    
def teste_nome_tipo_inteiro_engenheiro(criar_engenheiro):
    with pytest.raises (TypeError,match= "O nome deve ser um texto!")
    Engeneheiro(24,"719","Michel@",
                    Endereco("tancredo","25","casa","86615","salvador")
                              )
    
def teste_nome_vazio_engenheiro(criar_engenheiro):
    with pytest.raises (TypeError, match= "O nome estar vazio!")
    Engeneheiro("","719","Michel@",
                    Endereco("tancredo","25","casa","86615","salvador")
                              )