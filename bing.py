import pandas as pd
import requests
import json
import g4f
from g4f.Provider import (
    Bing,
)
 
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

def generate_ai_news(user):
  response = g4f.ChatCompletion.create(
      model=g4f.models.default,
      messages=[{"role": "Você agora é o tio patinhas",
                "content": f"Você agora é o tio patinhas, crie uma frase que apenas ele diria para {user['name']} e termine com - Tio Patinhas (max de 150 caracteres e coloque entre aspas, não use nenhum acento)"}],
      provider=Bing,
      auth=True
  )
  return response


for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"Usuário {user['name']} atualizado??? {success}!")
