from googletrans import Translator
import requests
# obs: para rodar esse código precisei fazer um downgrade pra versão 3.1.0a0 do googletrans 
# e usar o python 3.10 (a mais atual não tem cgi)
def fetch_data():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)
    # 200 é a porta http:
    return response.json() if response.status_code == 200 else None # operador ternário

def translate(lista):
    translator = Translator()
    translations = translator.translate(lista, src='en', dest='pt')
    return translations.text

characters = fetch_data()

if characters:
    for char in characters:
        name = char.get('name', '') # usei get para evitar erro caso se não tivesse
        translation_name = translate(name)
        char["name"] = translation_name

        affiliation = char.get('affiliation', '')
        translation_affiliation = translate(affiliation)
        char["affiliation"] = translation_affiliation

        print(char)
else:
    print("Failed to fetch data")
