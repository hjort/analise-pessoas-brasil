from genero_nome_pb2 import GeneroNomeRequest
from genero_nome_server import GeneroNomePreditor

def test_nome_nulo():
    service = GeneroNomePreditor()
    request = GeneroNomeRequest(nome=None)
    response = service.PreverGeneroNome(request, None)
    assert response.genero == -1

def test_nome_vazio():
    service = GeneroNomePreditor()
    request = GeneroNomeRequest(nome='')
    response = service.PreverGeneroNome(request, None)
    assert response.genero == -1

def test_nome_feminino():
    service = GeneroNomePreditor()
    request = GeneroNomeRequest(nome='MARIA')
    response = service.PreverGeneroNome(request, None)
    assert response.genero == 0

def test_nomes_femininos():
    nomes = ['Maria', 'SOCORRO', 'Leonor', 'Esther', 'Domingas', 'Conceicao']
    service = GeneroNomePreditor()
    for nome_pessoa in nomes:
        request = GeneroNomeRequest(nome=nome_pessoa)
        response = service.PreverGeneroNome(request, None)
        assert response.genero == 0

def test_nome_masculino():
    service = GeneroNomePreditor()
    request = GeneroNomeRequest(nome='JOAO')
    response = service.PreverGeneroNome(request, None)
    assert response.genero == 1

def test_nomes_masculinos():
    nomes = ['Joao', 'JOSE', 'Djalma', 'JURACY', 'ATILA', 'Valdir']
    service = GeneroNomePreditor()
    for nome_pessoa in nomes:
        request = GeneroNomeRequest(nome=nome_pessoa)
        response = service.PreverGeneroNome(request, None)
        assert response.genero == 1
