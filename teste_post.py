import requests
from rest_framework import status

headers = {'Authorization': 'Token 1cf682e4586c919a1a2e72e83fb8a1e074a2d8dd'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Curso exemplo",
    "url": "http://gerenciaexemplo.com.br"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

assert resultado.status_code == status.HTTP_201_CREATED

