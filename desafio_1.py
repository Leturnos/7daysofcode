import requests

def fetch_data():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(url)

    # 200 é a porta http
    return response.json() if response.status_code == 200 else None # operador ternário

characters = fetch_data()

if characters:
    for character in characters:
        print(character)
else:
    print("Failed to fetch data")