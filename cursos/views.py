from rest_framework import generics, viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import ehSuperUser

"""
API V1
"""


class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.queryset,
                                     curso_id=self.kwargs.get('curso_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.queryset, pk=self.kwargs.get('avaliacao_pk'))

"""
API V2
"""


class CursoViewSet(viewsets.ModelViewSet):
    #permission_classes = (
    #    ehSuperUser,
    #    permissions.DjangoModelPermissions
    #)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        curso = self.get_object()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""

# Utilizando cada mixin para cada operação
class AvaliacaoViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

