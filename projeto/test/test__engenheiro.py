import pytest 
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.UnidadeFederativa import unidade_federativa

@pytest.fixture
def criar_engenheiro():
    engenheiro1 = compile
    return engenheiro1
    
def teste_nome_tipo_inteiro_engenheiro(criar_engenheiro):
    with pytest.raises (TypeError,match= "O nome deve ser um texto!"):
        Engenheiro(4787, "719", "Michel@",
                   Endereco("tancredo", "25", "casa", "86615", "salvador",unidade_federativa.RIO_DE_JANEIRO), Sexo.MASCULINO, "456123")
    
def teste_nome_vazio_engenheiro(criar_engenheiro):
    with pytest.raises (TypeError, match= "O nome estar vazio!"):
        Engenheiro("", "719", "Michel@", 
                   Endereco("tancredo", "25", "casa", "86615", "salvador", unidade_federativa.SAO_PAULO), Sexo.MASCULINO, "456123")