from django.db import models

# Create your models here.

class Movie(models.Model):
    # Opções para fazer um dropdown para genero
    gender_action = 'ac'
    gender_fiction = 'fc'
    gender_adventure = 'ad'
    gender_comedy = 'cm'
    gender_drama = 'dr'
    gender_romance = 'ro'
    gender_options = [
        (gender_action, 'Action'),
        (gender_fiction, 'Fiction'),
        (gender_adventure, 'Adventure'),
        (gender_comedy, 'Comedy'),
        (gender_drama, 'Drama'),
        (gender_romance, 'Romance'),
    ]

    name = models.CharField(max_length=120) # Todo CharField precisa ter max_length, se não ele quebra
    genre = models.CharField(max_length=2, choices=gender_options, default=gender_action)
    sinopsis = models.TextField()
    release = models.DateField()
    runtime = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    # Para salvar imagens, necessário instalar o Pillow
    poster = models.ImageField(upload_to='') # Essa pasta será criada na raíz

    def __str__(self):
        return self.name