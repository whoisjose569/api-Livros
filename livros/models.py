from django.db import models

# Create your models here.

class Livro(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Autor', on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    year_of_publication = models.IntegerField()
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
    
    def __str__(self):
        return self.title
    

class Autor(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    
    def __str__(self):
        return self.name