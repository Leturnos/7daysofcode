from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator
from googletrans import Translator
import requests
from appdesafio4.models import Personagem

def fetch_data():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def translate(texto):
    translator = Translator()
    try:
        translation = translator.translate(texto, src='en', dest='pt')
        return translation.text
    except Exception as e:
        print(f"Erro na tradução de '{texto}': {e}")
        return texto  # Retorna o original em caso de erro

def index(request):
    characters = fetch_data()

    if characters:
        # deleta os arquivos do sqlite: (fiz isso para que o id seja zerado)
        if Personagem.objects.exists():
            Personagem.objects.all().delete()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='appdesafio4_personagem';")

        
        for char in characters:
            name = char.get('name', '') # usei get para evitar erro caso se não tivesse
            affiliation = char.get('affiliation', '')
            allies = ", ".join(char.get('allies', [])) # join vai converter de lista para string
            enemies = ", ".join(char.get('enemies', []))

            translation_name = translate(name)
            translation_affiliation = translate(affiliation)

            Personagem.objects.create(
                nome=translation_name,
                afiliacao=translation_affiliation,
                aliados=allies,
                inimigos=enemies
            )
    
        cards = Personagem.objects.all().order_by('id')
        paginator = Paginator(cards, 6) # 6 cards por página
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        return render(request, 'appdesafio4/index.html', {'cards': posts})
    else:
        return HttpResponse("Failed to fetch data")
