from googletrans import Translator
import requests, asyncio
"""Por causa do erro do coroutine tive que usar asyncio,
só depois de feito que vi que recomendaram usar a versão 3.1.010 kkkk
"""

def fetch_data():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)
    # 200 é a porta http:
    return response.json() if response.status_code == 200 else None # operador ternário

def translate(list):
    translator = Translator()
    translations = translator.translate(list, src='en', dest='pt')
    return translations

async def main():
    characters = fetch_data()

    if characters:
        for char in characters:
            name = char.get('name', '') # usei get para evitar erro caso se não tivesse
            affiliation = char.get('affiliation', '')

            text_translate = []
            if name:
                text_translate.append(name)
            if affiliation:
                text_translate.append(affiliation)

            if text_translate:
                translations = await translate(text_translate)

                # resultados:
                if name:
                    print(f"Nome: {name} -> {translations[0].text}")
                if affiliation:
                    print(f"Afiliação: {affiliation} -> {translations[1].text}")
                print() # pula uma linha
    else:
        print("Failed to fetch data")

asyncio.run(main())