from django.contrib import admin  # Importação do admin
from django.contrib.auth import views as auth_views
from django.urls import path, include  # Importação do include para múltiplos apps

from core.views import dashboard  # Importação da view do dashboard

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),  # Adiciona a URL do admin Django
]
