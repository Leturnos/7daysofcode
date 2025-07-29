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
    if characters:
        resultado = ""
        for char in characters:
            name = char.get('name', '') # usei get para evitar erro caso se não tivesse
            translation_name = translate(name)
            
            affiliation = char.get('affiliation', '')
            translation_affiliation = translate(affiliation)

            allies = char.get('allies', '')

            enemies = char.get('enemies', '')

            resultado += f"<p><b>Nome:</b> {translation_name}<br>"
            resultado += f"<b>Afiliação:</b> {translation_affiliation}<br>"
            resultado += f"<b>Aliados:</b> {allies}<br>"
            resultado += f"<b>Inimigos:</b> {enemies}</p><hr>"

        return HttpResponse(resultado)
    else:
        return HttpResponse("Failed to fetch data")
