from rest_framework.serializers import ModelSerializer
from livros.models import Livro, Autor

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('title', 'author', 'genre', 'year_of_publication')

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ('name',)