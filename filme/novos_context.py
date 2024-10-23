from .models import Filme
from filme.models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_filmes_recentes": lista_filmes}

def  lista_filmes_populares(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacao')[0:8]
    filme_destaque = lista_filmes[0]
    return {"lista_filmes_populares": lista_filmes, "filme_destaque": filme_destaque}

def lista_kids(request):
    lista_filmes = Filme.objects.filter(categoria='Desenhos')
    return {"lista_kids": lista_filmes}

def lista_anime(request):
    lista_filmes = Filme.objects.filter(categoria='Anime')
    return {"lista_anime": lista_filmes}

def lista_esport(request):
    lista_filmes = Filme.objects.filter(categoria='Esportes')
    return {"lista_esport": lista_filmes}

def lista_suspense(request):
    lista_filmes = Filme.objects.filter(categoria='Suspense')
    return {"lista_suspense": lista_filmes}

def lista_acao(request):
    lista_filmes = Filme.objects.filter(categoria='Ação')
    return {"lista_acao": lista_filmes}

def lista_aventura(request):
    lista_filmes = Filme.objects.filter(categoria='Aventura')
    return {"lista_aventura": lista_filmes}

def lsita_comedia(request):
    lista_filmes = Filme.objects.filter(categoria='Comédia')
    return {"lista_comedia": lista_filmes}

def lista_drama(request):
    lista_filmes = Filme.objects.filter(categoria='Drama')
    return {"lista_drama": lista_filmes}

def lista_ficcao(request):
    lista_filmes = Filme.objects.filter(categoria='Ficção')
    return {"lista_ficcao": lista_filmes}

def lista_romance(request):
    lista_filmes = Filme.objects.filter(categoria='Romance')
    return {"lista_romance": lista_filmes}

def lista_terror(request):
    lista_filmes = Filme.objects.filter(categoria='Terror')
    return {"lista_terror": lista_filmes}

def lista_familia(request):
    lista_filmes = Filme.objects.filter(categoria='Família')
    return {"lista_familia": lista_filmes}