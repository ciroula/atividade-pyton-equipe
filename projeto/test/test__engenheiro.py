import pytest 
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.UnidadeFederativa import unidade_federativa

@pytest.fixture
def criar_engenheiro():
    engenheiro1 = Engenheiro("Michel", "719", "Michel@", 
                   Endereco("tancredo", "25", "casa", "86615", "salvador", unidade_federativa.SAO_PAULO), Sexo.MASCULINO, "456123")
    return engenheiro1

def test_criar_engenheiro_nome(criar_engenheiro):
    assert criar_engenheiro.nome == "Michel"

def test_engenheiro_exemplo_numero(criar_engenheiro):
    assert criar_engenheiro.telefone == "719"

def test_criar_engenheiro_email(criar_engenheiro):
    assert criar_engenheiro.email == "Michel@"

def test_criar_engenheiro_crm(criar_engenheiro):
    assert criar_engenheiro.crea == "456123"

def test_criar_engenheiro_endereco_logradouro(criar_engenheiro):
    assert criar_engenheiro.endereco.logradouro == "tancredo"

def test_criar_engenheiro_endereco_numero(criar_engenheiro):
    assert criar_engenheiro.endereco.numero == "25"

def test_criar_engenheiro_endereco_complemento(criar_engenheiro):
    assert criar_engenheiro.endereco.complemento == "casa"

def test_criar_engenheiro_endereco_cep(criar_engenheiro):
    assert criar_engenheiro.endereco.cep == "86615"

def test_criar_engenheiro_endereco_cidade(criar_engenheiro):
    assert criar_engenheiro.endereco.cidade == "salvador"

    
def teste_nome_tipo_inteiro_engenheiro():
    with pytest.raises (TypeError,match= "O nome deve ser um texto!"):
        Engenheiro(4787, "719", "Michel@",
                   Endereco("tancredo", "25", "casa", "86615", "salvador",unidade_federativa.RIO_DE_JANEIRO), Sexo.MASCULINO, "456123")
    
def teste_nome_vazio_engenheiro():
    with pytest.raises (TypeError, match= "O nome estar vazio!"):
        Engenheiro("", "719", "Michel@", 
                   Endereco("tancredo", "25", "casa", "86615", "salvador", unidade_federativa.SAO_PAULO), Sexo.MASCULINO, "456123")