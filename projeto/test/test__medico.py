import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.UnidadeFederativa import unidade_federativa

@pytest.fixture
def medico_exemplo():
    medico1 = Medico("Fabíolo", "0800", "fabiolo@gmail.com",
                     Endereco("Rua a", "89", "Proximo ao mercado", "80125.405", "Fortaleza",unidade_federativa.SAO_PAULO),Sexo.MASCULINO, "456123")
    return medico1

def test_medico_exemplo_nome(medico_exemplo):
    assert medico_exemplo.nome == "Fabíolo"

def test_medico_exemplo_numero(medico_exemplo):
    assert medico_exemplo.telefone == "0800"

def test_medico_exemplo_email(medico_exemplo):
    assert medico_exemplo.email == "fabiolo@gmail.com"

def test_medico_exemplo_crm(medico_exemplo):
    assert medico_exemplo.crm == "456123"

def test_medico_exemplo_endereco_logradouro(medico_exemplo):
    assert medico_exemplo.endereco.logradouro == "Rua a"

def test_medico_exemplo_endereco_numero(medico_exemplo):
    assert medico_exemplo.endereco.numero == "89"

def test_medico_exemplo_endereco_complemento(medico_exemplo):
    assert medico_exemplo.endereco.complemento == "Proximo ao mercado"

def test_medico_exemplo_endereco_cep(medico_exemplo):
    assert medico_exemplo.endereco.cep == "80125.405"

def test_medico_exemplo_endereco_cidade(medico_exemplo):
    assert medico_exemplo.endereco.cidade == "Fortaleza"

def test_verifica_nome_tipo_medico():
    with pytest.raises(TypeError, match = "O nome deve ser um texto!"):
        Medico(8754, "0800", "fabiolo@gmail.com",
               Endereco("Rua a", "89", "Proximo ao mercado", "80125.405", "Fortaleza",unidade_federativa.SAO_PAULO),Sexo.MASCULINO, "456123")