from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

CATEGORIAS = [
    ("DESENHOS", "Desenhos"),
    ("FILMES", "Filmes"),
    ("ESPORTE", "Esportes"),
    ("CANAL_ABERTO", "Canais Abertos"),
    ("SUSPENSE", "Suspense"),
    ("ANIME", "Anime"),
    ("ACAO", "Ação"),
    ("AVENTURA", "Aventura"),
    ("COMEDIA", "Comédia"),
    ("DRAMA", "Drama"),
    ("FANTASIA", "Fantasia"),
    ("FICCAO_CIENTIFICA", "Ficção Científica"),
    ("ROMANCE", "Romance"),
    ("TERROR", "Terror"),
    ("FAMILIA", "Família"),
]

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=50)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=22, choices=CATEGORIAS)
    visualizacao = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodio", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    video = models.URLField()
    
    def __str__(self):
        return self.filme.titulo + ': ' + self.titulo
    
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")