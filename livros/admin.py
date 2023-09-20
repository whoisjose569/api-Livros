from django.contrib import admin
from .models import Livro, Autor

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'year_of_publication']

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['name']
