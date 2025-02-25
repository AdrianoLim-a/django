
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("Olá, esta é a página inicial do app Polls!")

def minha_view(request):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(f"<h1>Olá, Django!</h1><p>Data e hora atual: {agora}</p>")

def segunda_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página Estilizada</title>
        <style>
            body {
                background-color: #1e1e2f;
                color: white;
                text-align: center;
                font-family: Arial, sans-serif;
                padding: 20px;
            }
            h1 {
                color: #ffcc00;
            }
            .container {
                margin-top: 50px;
            }
            img {
                width: 300px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
            }
            .btn {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #ffcc00;
                color: #1e1e2f;
                text-decoration: none;
                font-weight: bold;
                border-radius: 5px;
            }
            .btn:hover {
                background-color: #ffaa00;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bem-vindo à Página Estilizada</h1>
            <p>Esta página contém cores, imagens e um botão estilizado!</p>
            <img src="https://source.unsplash.com/400x300/?nature,water" alt="Imagem Aleatória">
            <br>
            <a href="/" class="btn">Voltar para o início</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)