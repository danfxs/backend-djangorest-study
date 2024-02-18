import requests
from rest_framework import status

headers = {'Authorization': 'Token 1cf682e4586c919a1a2e72e83fb8a1e074a2d8dd'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "id": 1,
    "titulo": "AutoCARd",
    "url": "http://autocard.com.br"
}

resultado = requests.put(url=f'{url_base_cursos}1/', headers=headers, data=curso_atualizado)

assert resultado.status_code == status.HTTP_200_OK

cursos_1 = requests.get(url=f'{url_base_cursos}1/', headers=headers)
print(cursos_1.json())