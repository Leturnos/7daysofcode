from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator
import requests
# obs: para rodar esse código precisa usar versão 3.1.0a0 do googletrans 
# e usar o python 3.10 (a mais atual não tem cgi)
# 

def fetch_data():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)
    # 200 é a porta http:
    return response.json() if response.status_code == 200 else None # operador ternário

def translate(lista):
    translator = Translator()
    translations = translator.translate(lista, src='en', dest='pt')
    return translations.text

def index(request): # função chamada automaticamente quando alguém acessa a página
    characters = fetch_data()
    cards = []

    if characters:
        for char in characters:
            name = char.get('name', '')
            translation_name = translate(name)

            affiliation = char.get('affiliation', '') # usei get para evitar erro caso se não tivesse
            translation_affiliation = translate(affiliation)

            allies = ", ".join(char.get('allies', [])) # join vai converter de lista para string
            
            enemies = ", ".join(char.get('enemies', []))

            cards.append({
                'name': translation_name,
                'affiliation': translation_affiliation,
                'allies': allies,
                'enemies': enemies
            })

        return render(request, 'appdesafio4/index.html', {'cards': cards})
    else:
        return HttpResponse("Failed to fetch data")
