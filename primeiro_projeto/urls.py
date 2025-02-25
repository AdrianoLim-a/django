from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import reverse

def home(request):
    link = reverse('minha_view') 
    return HttpResponse(f'Página inicial funcionando! <a href="{link}">Ir para Minha View</a>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls', )),
    path('', home),  # Adiciona a página inicial
    path('', include('polls.urls')),
    
]