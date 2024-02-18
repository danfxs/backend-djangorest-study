import requests
from rest_framework import status

class TestCurso:
    headers = {'Authorization': 'Token 1cf682e4586c919a1a2e72e83fb8a1e074a2d8dd'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == status.HTTP_200_OK

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)
        assert curso.status_code == status.HTTP_200_OK

    def test_post_curso(self):
        novo = {
            "titulo": "Curso exemplo 2",
            "url": "http://gerenciaexemplo3.com.br"
        }
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == status.HTTP_201_CREATED
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            "id": 1,
            "titulo": "AutoCAd",
            "url": "http://autocad.com.br"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}1/', headers=self.headers, data=curso_atualizado)
        assert resposta.status_code == status.HTTP_200_OK

    def test_put_titulo_curso(self):
        curso_atualizado = {
            "id": 1,
            "titulo": "AutoCAd",
            "url": "http://autocad.com.br"
        }
        resposta = requests.put(url=f'{self.url_base_cursos}1/', headers=self.headers, data=curso_atualizado)
        assert resposta.json()['titulo'] == curso_atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}1/', headers=self.headers)
        assert resposta.status_code == status.HTTP_204_NO_CONTENT
        assert len(resposta.text) == 0