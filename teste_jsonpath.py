import jsonpath
import requests

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

resultado = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resultado)

nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)
print([d.get('nome') for d in avaliacoes.json()['results']])

primeiro_nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(primeiro_nome)
print([avaliacoes.json()['results'][0]['nome']])
