from django.urls import path, reverse_lazy
from .views import Homepage, HomeFilmes, DetalhesFilme, PesquisarFilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('browse', HomeFilmes.as_view(), name='homefilmes'),
    path('browse/jbv=<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),
    path('search/', PesquisarFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('ManageProfiles/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('CreatAcount/', Criarconta.as_view(), name='criarconta'),
    path('ChangePassword/', auth_view.PasswordChangeView.as_view(template_name='editaperfil.html',
                                                                 success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]