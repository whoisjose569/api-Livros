from livros.models import Livro , Autor
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from livros.api.serializers import LivroSerializer, AutorSerializer

class LivroViewSet(ModelViewSet):
    serializer_class = LivroSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','genre']
    queryset = Livro.objects.all()
    
    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        genre = self.request.query_params.get('genre', None)
        queryset = Livro.objects.all()

        if title:
            queryset = queryset.filter(title=title)
        
        if genre:
            queryset = queryset.filter(genre=genre)

        return queryset
    


class AutorViewSet(ModelViewSet):
    serializer_class = AutorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]
    queryset = Autor.objects.all()