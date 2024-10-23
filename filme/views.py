from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from .forms import CriarContaForm, FormHomepage
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from .models import Filme
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuario


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
         return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Adiciona a lista de filmes da categoria "Desenhos"
        context['lista_kids'] = Filme.objects.filter(categoria='DESENHOS')
        context['lista_anime'] = Filme.objects.filter(categoria='ANIME')
        context['lista_esport'] = Filme.objects.filter(categoria='ESPORTE')
        context['lista_suspense'] = Filme.objects.filter(categoria='SUSPENSE')
        context['lista_acao'] = Filme.objects.filter(categoria='ACAO')
        context['lista_aventura'] = Filme.objects.filter(categoria='AVENTURA')
        context['lista_comedia'] = Filme.objects.filter(categoria='COMEDIA')
        context['lista_drama'] = Filme.objects.filter(categoria='DRAMA')
        context['lista_ficcao'] = Filme.objects.filter(categoria='FICCAO_CIENTIFICA')
        context['lista_romance'] = Filme.objects.filter(categoria='ROMANCE')
        context['lista_terror'] = Filme.objects.filter(categoria='TERROR')
        context['lista_familia'] = Filme.objects.filter(categoria='FAMILIA')
        
        return context
    

class DetalhesFilme(LoginRequiredMixin, DetailView):
    template_name = "datalhesfilmes.html"
    model = Filme
    
    def get(self, request, *args, **kwargs):
        # contabiliza visualizacao
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[1:14]
        context["filmes_relacionados"] = filmes_relacionados
        return context
        
class PesquisarFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme
    
    def get_queryset(self):
        pesquisa = self.request.GET.get('q')
        if pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else:
            return None
    
class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editaperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
    
    def get_success_url(self):
        return reverse('filme:homefilmes')
    
class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('filme:login')
    
'''
Create your views here.
def homepage(request):
    return render(request, "homepage.html")


def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all()
    context['lista_filmes'] = lista_filmes
    return render(request, "homefilmes.html", context)
'''