import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco

@pytest.fixture
def medico_exemplo():
    medico1 = Medico("Fabíolo", "0800", "fabiolo@gmail.com", "455698", Endereco("Rua a", "89", "Proximo ao mercado", "80125.405", "Fortaleza"))
    return medico1

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.nome == "Fabíolo"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.numero == "0800"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.email == "fabiolo@gmail.com"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.crm == "455698"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.logradouro == "Rua a"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.numero == "89"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.complemento == "Proximo ao mercado"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.cep == "80125.405"

def test_medico_exemplo(medico_exemplo):
    assert medico_exemplo.endereco.cidade == "Salvador"

def test_verifica_nome_tipo_medico():
    with pytest.raises(TypeError, match = "Digite um nome valido."):
        Medico (456, "0800", "fabiolo@gmail.com", "455698", 
                Endereco("Rua a", "89", "Proximo ao mercado", "80125.405", "Fortaleza"))
