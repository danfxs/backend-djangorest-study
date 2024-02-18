import requests #pip install requests

# GET Avaliações

avaliacoes = requests.get("http://localhost:8000/api/v2/avaliacoes/")

# Acessando o código de status HTTP
#print(avaliacoes.status_code)

# Acessando dados de resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json())

# Acessando quantidade de registros
if 'count' in avaliacoes.json():
    print(avaliacoes.json()['count'])
else:
    print('Nao existe count em avaliacoes.json()')

# Acessando próxima página de registros
#print(requests.get(avaliacoes.json()['next']))

# Elementos de retorno
if 'results' in avaliacoes.json():
    print(avaliacoes.json()['results'])
    print(avaliacoes.json()['results'][0])
else:
    print('Nao existe results em avaliacoes.json()')
    print(avaliacoes.json())

avaliacao = requests.get("http://localhost:8000/api/v2/avaliacoes/1/")

print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token 1cf682e4586c919a1a2e72e83fb8a1e074a2d8dd'}

cursos = requests.get(url="http://localhost:8000/api/v2/cursos/", headers=headers)

print(cursos.status_code)
print(cursos.json())