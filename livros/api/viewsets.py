from livros.models import Livro , Autor
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from livros.api.serializers import LivroSerializer, AutorSerializer

class LivroViewSet(ModelViewSet):
    serializer_class = LivroSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author', 'genre', 'year_of_publication']
    queryset = Livro.objects.all()
    
    


class AutorViewSet(ModelViewSet):
    serializer_class = AutorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]
    queryset = Autor.objects.all()