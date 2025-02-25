
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Olá, esta é a página inicial do app Polls!")

def minha_view(request):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(f"<h1>Olá, Django!</h1><p>Data e hora atual: {agora}</p>")
